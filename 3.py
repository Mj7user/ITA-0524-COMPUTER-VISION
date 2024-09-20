import cv2

image = cv2.imread(r'C:\Users\MONISH\Pictures\images.jpeg')

larger_image = cv2.resize(image, (800, 600)) 
smaller_image = cv2.resize(image, (200, 150))  

cv2.imshow('Larger Image', larger_image)
cv2.imshow('Smaller Image', smaller_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()
