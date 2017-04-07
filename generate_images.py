import os
import sys
import cv2
import random
import shutil
import numpy as np
import re

def GetAllFilesList(path, extensions):
    files = [os.path.join(path, fn) for fn in next(os.walk(path))[2]]
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





possible_images = ['.jpg', '.png']
d = './images'
images_subdirs = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

if os.path.exists('./portfolio/index.md'):
    shutil.rmtree('./portfolio/index.md')

data = ''
with open('portfolio/index_temp.md', 'r') as file:
    data = file.read()

    occurs = [m.start() for m in re.finditer('<details', data)]
    print('occurs', occurs)

    for indx in occurs:
        det_html = data[indx : data.find('>', indx) + 1]
        print('det_html', det_html)
        if 'screenshot' in det_html:
            det_id = det_html[det_html.find('id=\"') + 4 : det_html.rfind('\"')]
            print('id: ', det_id)
            for subdir in images_subdirs:
                if det_id in subdir:
                    images = GetAllFilesList(subdir, possible_images)
                    images = list([img.replace('.', '') for img in images])
                    for img in images:
                        det_html += " <img src=\"" + img + "\" class=\"img-boarded\">";
                        print('det_html', det_html)
            data = data[: indx] + det_html + data[data.find('>', indx) + 1 : ]

with open('./portfolio/index.md', 'w') as f:
    f.write(data)
