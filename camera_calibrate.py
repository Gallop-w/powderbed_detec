import cv2
import numpy as np
import glob

def get_ROI(img_path):
    img = cv2.imread(img_path)
    img_dst = img[230:2400, 735:3100]
    return img_dst

# 1.提取角点
img = get_ROI('62-10.png')
img_dst, corners = cv2.findChessboardCorners(img, (13,13), None)

cv2.cornerSubPix(img_dst, corners)

img_dst = cv2.drawChessboardCorners(img, (13,13), corners, img_dst)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera()

# 显示结果
cv2.namedWindow('img_dst', 0)
# cv2.resizeWindow('img_dst', int(width/5), int(height/5))
cv2.imshow('img_dst', img_dst)
cv2.waitKey(0)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()



# 6.写入结果
# cv2.imwrite("./result_img/{}.png".format(img_path.split('.png')[0]+'cali'), img_dst)