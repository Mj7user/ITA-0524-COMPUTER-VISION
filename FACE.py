import cv2
img=cv2.imread(r'C:\Users\MONISH\Pictures\images.jpeg')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
HRC=cv2.CascadeClassifier(r'C:\Users\MONISH\Desktop\python\haarcascade_frontalface_default.xml')
fr=HRC.detectMultiScale(grey,1.1,5)
for(x,y,w,h) in fr:
    cv2.rectangle(img,(x,y),(x+w , y+h),(0,255,0),2)
cv2.imshow('img',img)
HRC1=cv2.CascadeClassifier(r'C:\Users\MONISH\Desktop\python\haarcascade_eye.xml')
eye=HRC1.detectMultiScale(grey,1.2,10)
for(x,y,w,h) in eye:
    cv2.rectangle(img,(x,y),(x+w , y+h),(0,0,255),2)
cv2.imshow('img',img)
HRC2=cv2.CascadeClassifier(r'C:\Users\MONISH\Desktop\python\haarcascade_smile.xml')
smile=HRC2.detectMultiScale(grey,2.5,10)
for(x,y,w,h) in smile:
    cv2.rectangle(img,(x,y),(x+w , y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
