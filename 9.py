import cv2
import numpy as np

def apply_erosion(image_path):
    image = cv2.imread(image_path)

    kernel = np.ones((3, 3), np.uint8)
    
    eroded_image = cv2.erode(image, kernel, iterations=1)
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Eroded Image', eroded_image)
    
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

apply_erosion(r'C:\Users\MONISH\Pictures\images.jpeg')
