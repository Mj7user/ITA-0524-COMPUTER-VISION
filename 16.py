import cv2
import numpy as np
def sobel_edge_detection(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image!")
        return
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    cv2.imshow('Original Image', img)
    cv2.imshow('Sobel X', sobel_x)
    cv2.imshow('Sobel Y', sobel_y)
    cv2.imshow('Sobel Combined', sobel_combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
sobel_edge_detection(r'C:\Users\MONISH\Pictures\images.jpeg')
