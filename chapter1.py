import cv2
import numpy as np
print("image ")
img = cv2.imread("index.jpeg")
kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imagCanny = cv2.Canny(img,150,100)
imageDialation = cv2.dilate(imagCanny, kernel, iterations= 5)
imageErdouded = cv2.erode(imageDialation, kernel, iterations= 1)
cv2.imshow("Gray image ", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("canny image", imagCanny)
cv2.imshow("dailation  image", imageDialation)
cv2.imshow("ERODE  image", imageErdouded)

cv2.waitKey(0)

