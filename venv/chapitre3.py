import  cv2
import  numpy as np

img = np.zeros((512,512,3), np.uint8)
#print(img.shape)
#img[200:300, 100:300] = 255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),7)
cv2.circle(img, (450,50),30,(0,255,255),5)
cv2.putText(img, "Opencv ", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
cv2.imshow("Image", img)

cv2.waitKey(0)



