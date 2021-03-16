from PIL import Image
from sys import argv
import os

a = argv[1]
b = argv[2]

try:
    os.mkdir(b)
    for files in os.listdir(a):
        im=Image.open(a+files)
        filename= os.path.splitext(files)[0]
        im.save(b+filename+'.png', 'png')
    print('Done!')
except FileExistsError:
    print('Folder Already Exists')



