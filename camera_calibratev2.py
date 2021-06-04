import cv2
import numpy as np
import glob

# # 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
# criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)
#
# # 获取标定板角点的位置
# objp = np.zeros((14 * 13, 3), np.float32)
# objp[:, :2] = np.mgrid[0:14, 0:13].T.reshape(-1, 2)  # 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y
#
# obj_points = []  # 存储3D点
# img_points = []  # 存储2D点
#
# images = glob.glob("chessboard/*.png")
# i=0;
# for fname in images:
#     img = cv2.imread(fname)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     size = gray.shape[::-1]
#     ret, corners = cv2.findChessboardCorners(gray, (14, 13), None)
#     #print(corners)
#
#     if ret:
#
#         obj_points.append(objp)
#
#         corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)  # 在原角点的基础上寻找亚像素角点
#         #print(corners2)
#         if [corners2]:
#             img_points.append(corners2)
#         else:
#             img_points.append(corners)
#
#         # cv2.drawChessboardCorners(img, (14, 13), corners, ret)  # 记住，OpenCV的绘制函数一般无返回值
#         # i+=1;
#         # cv2.imwrite('conimg'+str(i)+'.png', img)
#         # cv2.waitKey(1500)
#
# print(len(img_points))
# cv2.destroyAllWindows()
#
# # 标定
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)
#
# print("ret:", ret)
# print("mtx:\n", mtx) # 内参数矩阵
# print("dist:\n", dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
# print("rvecs:\n", rvecs)  # 旋转向量  # 外参数
# print("tvecs:\n", tvecs ) # 平移向量  # 外参数
#
# print("-----------------------------------------------------")

mtx = np.array([[4.83953298e+03, 0.00000000e+00, 1.93548592e+03],
        [0.00000000e+00, 4.84544333e+03, 1.47550908e+03],
         [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist = np.array([[-9.65379370e-02,  1.30139024e-02,  3.14773426e-04,  1.63575383e-04,  2.60987251e+00]])

img = cv2.imread("img_280-light/62-1.png")# images[3]
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))#显示更大范围的图片（正常重映射之后会删掉一部分图像）
print (newcameramtx)
print("------------------使用undistort函数-------------------")
dst = cv2.undistort(img,mtx,dist,None,newcameramtx)
x,y,w,h = roi
dst1 = dst[y:y+h,x:x+w]
cv2.imwrite('calibresult3.png', dst1)
print ("方法一:dst的大小为:", dst1.shape)



