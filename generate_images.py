import os
import sys
import random
import shutil
import numpy as np
import re

def GetAllFilesList(path, extensions):
    files = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]
    files.sort(key = lambda f: int(filter(str.isdigit, f)))
    files = filter(lambda file: 'directory' not in file, files)
    return list(filter(lambda file: sum([ext in file.lower() for ext in extensions]) > 0, files))

def GetAllFilesListRecusive(path, extensions):
    files_all = []
    for root, subFolders, files in os.walk(path):
        for name in files:
             # linux tricks with .directory that still is file
            if not 'directory' in name and sum([ext in name.lower() for ext in extensions]) > 0:
                files_all.append(os.path.join(root, name))
    return files_all


img_template = '''<div class="gallery"><a target="_blank" href="%img"><img src="%img" width="300" height="200"></a><div class="desc">%descr</div></div>'''

def getImageCode(img_path, descr = None):
    global img_template
    temp = img_template.replace('''%img''', img_path)

    if descr != None:
        temp = temp.replace('''%descr''', descr)

    return temp

possible_images = ['.jpg', '.png']
d = './images'
images_subdirs = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

if os.path.exists('./portfolio/index.md'):
    os.remove('./portfolio/index.md')

data = ''
with open('portfolio/index_temp.md', 'r') as file:
    data = file.read()

    occurs = [m.start() for m in re.finditer('<details', data)]
    print('occurs', occurs)

    start = 0
    while True:
        start = data.find('<details', start + 1)
        if start < 0:
            break
        det_html = data[start : data.find('>', start) + 1]
        #print('det_html', det_html)
        if 'screenshot' in det_html:
            det_id = det_html[det_html.find('id=\"') + 4 : det_html.rfind('\"')]
            print('id: ', det_id)
            for subdir in images_subdirs:


                if det_id in subdir:

                    images = GetAllFilesList(subdir, possible_images)

                    ####
                    descrs_files = GetAllFilesList(subdir, ['.descr', '.txt'])
                    descrs = {}
                    for d in descrs_files:
                        pure_name = d[d.rfind('/') + 1 : d.rfind('.')]
                        with open(d, 'r') as file:
                            descr = file.read().strip()
                            descrs[pure_name] = descr


                    # max_len = max(list([len(d) for d in descrs.values()])) if len(descrs) > 0 else 0
                    # for k in descrs.keys():
                    #     descrs[k] = descrs[k] + (' ' * (max_len - len(descrs[k])))
                    ####

                    print('descrs', descrs)

                    images = list([img[1:] for img in images])
                    for img in images:
                        pure_name = img[img.rfind('/') + 1 : img.rfind('.')]
                        descr = descrs[pure_name] if pure_name in descrs else 'No description'

                        print('getImageCode(img, descr):', getImageCode(img, descr))
                        det_html += getImageCode(img, descr)
                        #print('det_html', det_html)



            data = data[: start] + det_html + data[data.find('>', start) + 1 : ]

with open('./portfolio/index.md', 'w') as f:
    f.write(data)
