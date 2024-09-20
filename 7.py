import cv2

image = cv2.imread(r'C:\Users\MONISH\Pictures\images.jpeg')
rotated_image = cv2.flip(image, 0) 

cv2.imshow('Original Image', image)
cv2.imshow('180-Degree Rotated Image', rotated_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
