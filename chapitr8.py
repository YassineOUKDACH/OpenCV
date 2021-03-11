####
# FACE DETECTION
"""
POSITIVE FACES &&& NEGATIVES NON FACES
WE WILL TRAIN FOR OBTIN XML FILE
"""
import  cv2


faceCascade= cv2.CascadeClassifier("/home/yassine/PycharmProjects/Opencv/venv/lib/python3.8/site-packages/cv2/data/haarcascade_upperbody.xml")
img = cv2.imread("tv.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Image", img)


cv2.waitKey(0)