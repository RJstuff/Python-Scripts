import cv2

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

#Create a cascadeClassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("Photo0100.jpg")

#Convert to gray
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detect the coordinates of face
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

#For rectangle around the face
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
re_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("OFOCN",re_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

"""

img = cv2.imread("Photo0100.jpg")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

for x,y,w,h in face:
    gray_Photo0100img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
    
re_img = cv2.resize(gray_img , (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Prayag&ROMI",re_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

"""
