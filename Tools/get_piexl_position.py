import cv2

# 采样图片
img = cv2.imread("../64_rotate.png")


# print img.shape

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    5, (0, 0, 255), thickness=4)
        cv2.imshow("image", img)

height, width = img.shape[:2]
print(int(height/5), int(width/5))
cv2.namedWindow("image", 0)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.resizeWindow('image', int(width/5), int(height/5))
cv2.imshow("image", img)

while (True):
    try:
        cv2.waitKey(1)
    except Exception:
        cv2.destroyAllWindows()
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
