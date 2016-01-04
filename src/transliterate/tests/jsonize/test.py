#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 23, 2015

@author: schernikov
'''
import pkgutil, json, os, re, six
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
    ru_latin = translator('ru')
    print ru_latin

    #print ru_latin.encoder
    #print ru_latin.decoder

    s1 = u'Tра-ля-ля'
    print "%s -> %s"%(s1, ru_latin.encode(s1))
    s2 = u'bla-bla'
    print "%s -> %s"%(s2, ru_latin.decode(s2))
    
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

    return variant.codec()


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

    @property
    def id(self):
        return self._name
    
    @property
    def language(self):
        return self._lang
        
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
        return Codec(self._var, self._script.language.name, self._script.id, self.name)


class Codec(object):
    
    def __init__(self, vdict, lname, sname, vname, debug=False):
        self._lname = lname
        self._sname = sname
        self._vname = vname

        edups = {}
        ddups = {}
        emp = {}
        dec = {}
        for k, v in vdict.items():
            if type(v) == list: 
                for i in v:
                    self._apply(dec, ddups, i, k)
                self._apply(emp, edups, k, v[0])
            else:
                self._apply(dec, ddups, v, k)
                self._apply(emp, edups, k, v)

        if debug:
            nm = '%s.%s.%s'%(lname, sname, vname)
            self._showdups(nm, 'encoder', edups)
            self._showdups(nm, 'decoder', ddups)
        
        self._encoder = Translit(emp, 'encoder')
        self._decoder = Translit(dec, 'decoder')


    def _showdups(self, nm, tp, dups):
        if not dups: return
        print "%s: duplicate %s entries:"%(nm, tp)

        for k, lst in dups.items():
            print u'  %s->[%s]'%(k, ','.join(lst))
        print


    def _apply(self, mp, dups, k, v):
        subs = set(reslash.findall(v))
        if subs: # clean-out all escaped controls from target script
            for s in subs:
                v = v.replace(s, '')
        if mp.has_key(k):
            d = dups.get(k, None)
            if d is None:
                d = set()
                d.add(mp[k])
                dups[k] = d
            d.add(v)

        mp[k] = v
        
    def __str__(self):
        return "%s.%s.%s"%(self._lname, self._sname, self._vname)
        
    def encode(self, msg):
        return self._encoder.translit(msg)
    
    def decode(self, msg):
        return self._decoder.translit(msg)

    @property
    def encoder(self):
        return self._encoder
    
    @property
    def decoder(self):
        return self._decoder


class Translit(object):

    def __init__(self, mp, nm):
        self._name = nm
        regs = []
        orders = {}
        singles = {}
        for k, v in mp.items():
            if reslash.search(k): # check if it has regex controls
                if k[0] == '\\' and len(k) > 2:
                    uk = k[:2]+k[2].upper()+k[3:]
                    regs.append((re.compile(uk, re.UNICODE), v.capitalize()))
                regs.append((re.compile(k, re.UNICODE), v))
                continue
            if len(k) == 1 and len(v) == 1:
                singles[ord(k)] = ord(v)
                up = k.upper()
                if up != k: singles[ord(up)] = ord(v.upper())
                continue
            ordr = orders.get(len(k), None)
            if ordr is None:
                ordr = {}
                orders[len(k)] = ordr
            cap = k.capitalize()
            if k != cap: ordr[cap] = v.capitalize()
            ordr[k] = v
        maps = [orders[sz] for sz in sorted(orders.keys(), reverse=True)]
        self._regs = tuple(regs)
        self._subs = tuple(maps)
        self._trans = singles

    def translit(self, msg):
        if type(msg) != six.text_type: raise UnicodeError("Unicode is expected. Got %s"%(type(msg)))

        for reg, v in self._regs:
            msg = reg.sub(v, msg)
        
        for order in self._subs:
            for k, v in order.items():
                msg = msg.replace(k, v)

        return msg.translate(self._trans)

    def __unicode__(self):
        res = u'%s\n'%(self._name.capitalize())
        if self._regs:
            res += " Regexes:\n"
            for rr, v in self._regs:
                res += "  %s -> %s\n"%(rr.pattern, v)
            res += '\n'
        if self._subs:
            res += " Substitutes:\n"
            for sub in self._subs:
                kk = sub.keys()
                res += "  size %d:\n"%(len(kk[0]))
                for k in sorted(kk):
                    res += "    %s -> %s\n"%(k, sub[k])
                res += '\n'

        if self._trans:
            res += " Translates:\n"
            for k in sorted(self._trans.keys()):
                res += "  %s -> %s\n"%(unichr(k), unichr(self._trans[k]))
            res += '\n'

        return res
    
    def __str__(self, *args, **kwargs):
        return unicode(self).encode('utf-8')


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
