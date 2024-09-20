import cv2  
path = r'C:\Users\MONISH\Pictures\images.jpeg'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
cv2.imshow("GrayScale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
