import cv2

cap = cv2.VideoCapture('testV.mp4')


while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow("Vedio", frame)

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()