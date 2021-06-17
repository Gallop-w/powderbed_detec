import cv2
import numpy as np
from PIL import Image

img_path = '1_0.jpeg'
img = Image.open(img_path)
img_rot = img.rotate(-1.50)
# img_rot.save('1_0_rotate.png')

img_origin = cv2.cvtColor(np.asarray(img_rot), cv2.COLOR_RGB2BGR)
height, width = img_origin.shape[:2]

# 2.图像坐标点，世界坐标点
src_point = np.float32([[1323, 719], [2966, 724],
                        [1260, 2385], [3082, 2382]])
dst_point = np.float32([[1323, 719], [2966, 719],
                        [1323, 2362], [2966, 2362]])


# 3.获取透视变换矩阵
perspective_matrix = cv2.getPerspectiveTransform(src_point, dst_point)

# 4.执行透视变换
img_dst = cv2.warpPerspective(img_origin, perspective_matrix, (width, height))

# 5.显示结果
# cv2.namedWindow('img_dst', 0)
# cv2.resizeWindow('img_dst', int(width/2.5), int(height/5))
# img_ret = np.hstack([img_origin, img_dst])
# cv2.imshow('img_dst', img_ret)
# cv2.waitKey(0)
# if cv2.waitKey(0)==27:
#     cv2.destroyAllWindows()

# 6.裁剪图片
img_dst = img_dst[80:2370,680:2980]

# 7.压缩图片
img_dst = cv2.resize(img_dst,(1000,1000))

# 8.写入结果
cv2.imwrite("./result_img/resize{}.jpg".format(img_path.split('.png')[0]), img_dst)

