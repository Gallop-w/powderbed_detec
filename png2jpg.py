import cv2
import numpy as np
import glob
from PIL import Image
import matplotlib as plt

ori_img = '1-4.png'
img_png = Image.open(ori_img)
print(img_png.mode)
bg = Image.new('RGB', img_png.size, (0,0,0))
bg.paste(img_png, img_png)
bg.save('test.jpg')


# cv2.imwrite("./result_img/{}.png".format(img_path.split('.png')[0]+'cali'), img_dst)
