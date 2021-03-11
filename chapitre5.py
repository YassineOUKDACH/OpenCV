import cv2
import numpy as np


img = cv2.imread("Lina.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hor = np.hstack((img, img,img))
ver = np.vstack((img,img,img ))

cv2.imshow("horizonal", hor)
cv2.imshow("vertical", ver)

cv2.waitKey(0)
