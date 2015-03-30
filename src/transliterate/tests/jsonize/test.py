'''
Created on Mar 23, 2015

@author: schernikov
'''
import pkgutil, json, os, re
import transliterate
import codecs
import transliterate.contrib.languages as langs
from transliterate.exceptions import LanguagePackNotFound

resub = re.compile('\{(?P<sub>[^\}]+)\}', re.UNICODE)
regroup = re.compile('\[(?P<list>[^\]]+)\]', re.UNICODE)
recontrol = re.compile('[\x00-\x1f]', re.UNICODE)
reslash = re.compile(r'(?P<ctrl>\\{1,1}[^\\])', re.UNICODE)
pycontrols = (r'\A', r'\b', r'\B', r'\Z')

def main():
    ru = translator('ru')
    codec = ru.codec()
    codec.show()
    #===========================================================================
    # for shorts in ru['latin']['shortcuts']:
    #     name = shorts['name']
    #     for nm in shorts.keys():
    #         if nm == 'name': continue
    #         print "%s: %s -> %s"%(name, nm, shorts[nm])
    #===========================================================================
    
    #pprint.pprint(ru['latin']['shortcuts'])
    
    #test(loc)

def ungroup(s):
    groups = []
    for m in regroup.finditer(s):
        groups.append(Group(m))
        
    return groups


def translator(language_code, script_name='latin', variant_name=None):

    lang = Language(language_code)
    
    script = lang.script(script_name)
    
    variant = script.variant(variant_name)

    variant.relist()

    variant.unshort()

    variant.ungroup()
    
    variant.uncontrol()

    return variant


def findmatches(variant, chars, script_name):
    mm = []
    for ch in chars:
        mchar = variant.get(ch, None)
        if not mchar: raise InvalidFormat("Can not find matching char for %s in %s" % (ch, script_name))
        if type(mchar) == list:
            mm.append(mchar[0])
        else:
            mm.append(mchar)

    return mm



class Language(object):
    location = os.path.join(os.path.dirname(transliterate.__file__), '..', '..', 'test')
    
    def __init__(self, name):
        self.name = name
        
    def script(self, sname):
        try:
            with open(os.path.join(self.location, '%s.json'%(self.name))) as f:
                tr = json.load(f)
        except:
            raise LanguagePackNotFound("Language pack for code %s is not found." % self.name)
    
        scr = tr.get(sname, None)
        if not scr:
            raise InvalidFormat("Language script %s from  %s pack is missing" % (sname, self.name))
        
        return Script(self, scr, sname)
        

class Script(object):
    
    def __init__(self, lang, scr, name):
        self._lang = lang
        self._script = scr
        self._name = name
        
    @property
    def name(self):
        return "%s[%s]"%(self._lang.name, self._name)
        
    def variant(self, vname):
        if not vname:
            vname = self._script.get('default', None)
    
        if not vname:
            raise InvalidFormat("Language script %s from %s pack is missing; default variant is not defined" % (self.name, self._lang.name))
    
        vv = self._script.get('variants', None)
        if vv is None:
            raise InvalidFormat("Language script %s from %s pack is missing variants definitions. Expecting %s" % (self.name, self._lang.name, vname))
        
        v = vv.get(vname, None)
        if v is None:
            raise InvalidFormat("Language script %s from  %s pack is missing expected variant %s" % (self.name, self._lang.name, vname))
        
        return Variant(self, v, vname)
    
    def shorts(self):
        return self._script.get('shortcuts', {})
        

class Variant(object):
    
    def __init__(self, script, var, name):
        self._script = script
        self.name = name
        self._var = var
        
    def relist(self):
        for k, v in self._var.items():
            if type(v) == list: continue
            parts = v.split()
            if len(parts) > 1:
                self._var[k] = parts
            
    def unshort(self):
        shorts = self._script.shorts()
        if not shorts: return

        newvar = {}
        for k, v in self._var.items():
            nk = self._reshort(shorts, k)
            if type(v) == list:
                newvar[nk] = [self._reshort(shorts, vl) for vl in v]
            else:
                newvar[nk] = self._reshort(shorts, v)

        self._var = newvar
        
    def _reshort(self, shorts, s):
        ss = []
        for m in resub.finditer(s):
            if m:
                sub = m.groupdict()['sub']
                sh = shorts.get(sub, None)
                if sh is None: raise InvalidFormat("Undefined shortcut %s in %s"%(sub, self._script.name))
                start, end = m.regs[0]
                ss.append((s[start:end], sh))
    
        for sub, rep in ss:
            s = s.replace(sub, rep)
    
        return s

        
    def ungroup(self):
        newvars = {}
        for k, v in self._var.items():
            kgs = ungroup(k)
            if type(v) == list:
                if len(kgs) != 0: raise InvalidFormat("Can not have groups and lists in the pair (%s, %s) in %s" % (k, v, self._script.name))
                newvars[k] = v
                continue
            vgs = ungroup(v)
            if len(kgs) == 0 and len(vgs) == 0:
                newvars[k] = v 
                continue
            if len(kgs) < len(vgs): raise InvalidFormat("Groups are not matching for %s and %s in %s" % (k, v, self._script.name))
            if len(kgs) > 1: raise InvalidFormat("Only one group per entry is supported. Found %d in %s from %s" % (len(kgs), k, self._script.name))
            kg = kgs[0]
            if len(vgs) == 0:
                self.unroll(newvars, k, kg, lambda idx: v)
                continue
            vg = vgs[0]
            if len(vg.set) == 1 and vg.set[0] == '.':
                vg.set = findmatches(self._var, kg.set, self._script.name)
                
            if len(kg.set) != len(vg.set):
                raise InvalidFormat("Groups must match in %s and %s from %s" % (k, v, self._script.name))
            
            pre = v[:vg.start]
            post = v[vg.stop:]
            def onv(idx):
                return pre + vg.set[idx] + post
            
            self.unroll(newvars, k, kg, onv)

        self._var = newvars

    def uncontrol(self):
        for k, v in self._var.items():
            self._checkcontr(k)
            
            if type(v) == list:
                for sv in v:
                    self._checkcontr(sv)
            else:
                self._checkcontr(v)

    def _checkcontr(self, val):
        m = recontrol.search(val)
        if m: raise InvalidFormat("No control chars are allowed. Got %s in %s. Use extra '\\' in json"%(val, self._script.name))
        for m in reslash.finditer(val):
            ctrl = m.groupdict()['ctrl']
            if not (ctrl in pycontrols): raise InvalidFormat("Only '%s' controls are allowed. Got '%s'"%(pycontrols, ctrl))
        
    def unroll(self, newvars, k, kg, onv):
        pre = k[:kg.start]
        post = k[kg.stop:]
        for idx in xrange(len(kg.set)):
            nk = pre + kg.set[idx] + post
            v = onv(idx)
            nv = newvars.get(nk, None)
            if nv is None:
                newvars[nk] = v
            else:
                if nv != v:
                    raise InvalidFormat("Warning: uncontrolled order of options %s or %s for %s in %s"%(nv, v, nk, self._script.name))
                
    def codec(self):
        mp = {}
        for k, v in self._var.items():
            if type(v) == list: v = v[0]
            subs = set(reslash.findall(v))
            if subs: # clean-out all escaped controls from target script
                for s in subs:
                    v = v.replace(s, '')
            mp[k] = v

        return Codec(mp)


class Codec(object):

    def __init__(self, mp):
        regs = []
        orders = {}
        singles = {}
        for k, v in mp.items():
            if reslash.search(k): # has regex controls
                regs.append((re.compile(k, re.UNICODE), v))
                continue
            if len(k) == 1:
                singles[k] = v
                continue
            ordr = orders.get(len(k), None)
            if ordr is None:
                ordr = {}
                orders[len(k)] = ordr
            ordr[k] = v
        maps = [orders[sz] for sz in sorted(orders.keys(), reverse=True)]
        self._regs = tuple(regs)
        self._subs = tuple(maps)
        self._trans = singles

    def transcode(self, msg):
        #TODO finish
        return msg
    
    def show(self):
        if self._regs:
            print "Regexes:"
            for rr, v in self._regs:
                print "  %s -> %s"%(rr.pattern, v)
            print
        if self._subs:
            print "Substitutes:"
            for sub in self._subs:
                kk = sub.keys()
                print "  size %d:"%(len(kk[0]))
                for k in sorted(kk):
                    print "    %s -> %s"%(k, sub[k])
                print

        if self._trans:
            print "Translates:"
            for k in sorted(self._trans.keys()):
                print "  %s -> %s"%(k, self._trans[k])
            print 


class Group(object):
    
    def __init__(self, m):
        self.start, self.stop = m.regs[0]
        start, end = m.regs[1]
        self.set = [ch for ch in m.string[start:end]]


def test(loc):
    for loader, modnm, ispkg in pkgutil.walk_packages(langs.__path__, langs.__name__+'.'):
        if not modnm.endswith('.data.standard'): continue
        m = loader.find_module(modnm).load_module(modnm); ispkg
        name = modnm.split('.')[3]
        print name
        for nm in dir(m):
            if nm.startswith('__'): continue
            if nm == 'mapping':
                checkmapping(loc, name, m.mapping[0], m.mapping[1])
            print '  ',nm
    

def checkmapping(loc, name, lat, scr):
    if type(lat) != unicode or type(scr) != unicode:
        raise Exception('Unicode is expected')

    if len(lat) != len(scr):
        raise Exception('Same map sizes are expected')

    subscr = u''
    latscr = u''
    
    for pos in xrange(len(scr)):
        subscr += scr[pos] + ' '
        latscr += lat[pos] + ' '

    with codecs.open(os.path.join(loc, '%s.gen.json'%name), 'wb', 'utf-8') as f:
        json.dump({'base':subscr, 'latin':latscr}, f, ensure_ascii=False, separators=(',',':'))
    
    
class InvalidFormat(Exception):
    
    def __init__(self, msg):
        super(InvalidFormat, self).__init__(msg)
    
if __name__ == '__main__':
    main()