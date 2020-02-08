import os
import re
from pathlib import Path
from transliterate.discover import autodiscover
from transliterate import translit, get_available_language_codes
autodiscover()

root_dir = os.path.join('/', 'home', 'petro', 'dev', 'priv', 'lem-spiwnyk')
out_root = os.path.join('generated')

for root, _, files in os.walk(root_dir):
    rel_path = os.path.relpath(root, root_dir)
    out_path = os.path.join(out_root, rel_path)
    Path(out_path).mkdir(parents=True, exist_ok=True)
    for file in files:
        if file.endswith(".tex"):
            infile = os.path.join(root, file)
            outfile = os.path.join(out_path, file)
            with open (infile, 'r') as f:
                data = f.read()
                trans = translit(data, 'lem', reversed=True)
                with open (outfile, 'w') as of:
                    of.write(trans)

songs = []
for root, _, files in os.walk(out_root):
    rel_path = os.path.relpath(root, out_root)
    for file in files:
        if file.endswith(".tex"):
            infile = os.path.join(root, file)
            with open (infile, 'r') as f:
                first_line = f.readline()
                title = re.findall(r'\\subsection{(.*?)}', first_line)
                print(title)
                if title != []:
                    songs.append({'title' : title[0],
                                  'path' : os.path.join(rel_path, file)})
sorted = sorted(songs, key=lambda k: k['title'].lower()) 
print(sorted)

latin_file = out_root = os.path.join('generated', 'latin.tex')
with open(latin_file, 'w') as lf:
    lf.write('\\section{Pisni}\n')
    for song in sorted:
        lf.write('\\input{{{}}}\n'.format(song['path'].replace('.tex', '')))