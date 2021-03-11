import cv2
import numpy as np
## color detection
path = '/home/yassine/PycharmProjects/Opencv/lam.jpg'
def empty(a):
    pass
cv2.namedWindow("Trackbors")
cv2.resizeWindow("Trackbors", 640,240)
cv2.createTrackbar("hue Min", "Trackbors", 0,179, empty)
cv2.createTrackbar("hue Max", "Trackbors", 179,179, empty)
"""cv2.createTrackbar("sat1 Max", "Trackbors", 0,255, empty)
cv2.createTrackbar("sat2 Max", "Trackbors", 255,255, empty)
cv2.createTrackbar("sat3 Max", "Trackbors", 0,255, empty)
cv2.createTrackbar("sat4 Max", "Trackbors", 255,255, empty)"""

while True:

    img = cv2.imread(path)
    imgs =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h_min = cv2.getTrackbarPos("hue Min","Trackbors")
    h_max = cv2.getTrackbarPos("hue Max","Trackbors")
    """s_min = cv2.getTrackbarPos("sat Min","Trackbors")
    s_max = cv2.getTrackbarPos("sat Max","Trackbors")
    v_min = cv2.getTrackbarPos("val Min","Trackbors")
    v_max = cv2.getTrackbarPos("val Max","Trackbors")
    print(h_min, h_max, s_min,s_min,v_min,v_max)
    """
    print(h_min, h_max)

    """lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])"""
    lower = np.array([h_min])
    upper = np.array([h_max])
    mask = cv2.inRange(imgs, lower, upper)

    imageResulte = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow("Lam", img)
    cv2.imshow("HSV", imgs)
    cv2.imshow("MASK", mask)
    cv2.imshow("Resulte", imageResulte)


    cv2.waitKey(1)
