import cv2
path = r'C:\Users\MONISH\Pictures\images.jpeg'
img =cv2.imread(path,cv2.IMREAD_GRAYSCALE)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Img Blur",imgBlur)
cv2.waitKey(0)
