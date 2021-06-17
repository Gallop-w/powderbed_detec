import cv2

img_ori = cv2.imread('../result_img/calibresult3-1.png')
img_ori = img_ori[90:2420,600:3120]
cv2.namedWindow('img', 0)
cv2.imshow('img', img_ori)
cv2.waitKey(100)
if cv2.waitKey() == 27:
    cv2.destroyAllWindows()

cv2.imwrite('cut_img2.png', img_ori)


