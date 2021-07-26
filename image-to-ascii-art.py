from PIL import Image
import numpy as np
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
width = int(sys.argv[3])
height = int(sys.argv[4])
def color_to_ascii(color):#different color options
    if sys.argv[5]:
        if sys.argv[5] == 0:
            c = np.linalg.norm(color)
            return c * (len(pallete)/442)
        if sys.argv[5] == 1:
            c = max(color)
            return c * (len(pallete)/256)
    else:
        c = np.linalg.norm(color)
        return c * (len(pallete)/442)        

img = Image.open(input_file)
img = img.resize((width, height), Image.BILINEAR)
img = np.array(img)

pallete = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
with open(output_file, 'w+') as f:
    for i in img:
        for j in i:
            f.write(pallete[int(color_to_ascii(j))])
        f.write('\n')
        

