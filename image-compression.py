import sys
from PIL import Image


img=Image.open(sys.argv[1])
img=img.resize(img.size,Image.ANTIALIAS)
img.save(sys.argv[2])
 
