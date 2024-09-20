import cv2
import numpy as np

def apply_smoothing_filter(image_path, kernel_size):
    
    image = cv2.imread(image_path)
    
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    
    smoothed_image = cv2.filter2D(image, -1, kernel)
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Smoothed Image', smoothed_image)
    
    cv2.waitKey(0) 
    cv2.destroyAllWindows()  
apply_smoothing_filter(r'C:\Users\MONISH\Pictures\images.jpeg', 5)
