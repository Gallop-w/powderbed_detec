import cv2
import numpy as np
from PIL import Image

img = cv2.imread('../62-10.png')

im = Image.fromarray(img)
img_rot = im.rotate(-1.50)
img_rot.show()
img_rot.save('img_rotate.png')
