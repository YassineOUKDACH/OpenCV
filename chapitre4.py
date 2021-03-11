import cv2
import numpy as np
img = cv2.imread("rami.jpg")
width, hight = 250,350
pts1 = np.float32([[100,197],[287, 188],[154, 482],[352, 440]])
pts2 = np.float32([[0,0],[width,0],[0,hight], [width,hight]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput =  cv2.warpPerspective(img, matrix, (width,hight))
print(img.shape)
cv2.imshow("Image", img)
cv2.imshow("outpout", imgoutput)
cv2.waitKey(0)