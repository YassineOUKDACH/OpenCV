import cv2
import numpy as np
img = cv2.imread("Lina.jpg")
print(img.shape)
immResize = cv2.resize(img,(1000,500))
imgCroped = img[0:200, 200:500]
cv2.imshow("Lina", img)
cv2.imshow("Resize Image", immResize)
cv2.imshow("Croped Image", imgCroped)

print(immResize.shape)
cv2.waitKey(0)