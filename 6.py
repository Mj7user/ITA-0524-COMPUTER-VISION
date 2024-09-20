import cv2
image = cv2.imread(r'C:\Users\MONISH\Pictures\images.jpeg')
rotated_image = cv2.transpose(image)
rotated_image = cv2.flip(rotated_image, 1)   
cv2.imshow('Original Image', image)
cv2.imshow('90-Degree Clockwise Rotated Image', rotated_image)

cv2.waitKey(0)  
cv2.destroyAllWindows()
