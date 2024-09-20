import cv2
import numpy as np
def roberts_edge_detection(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image!")
        return
    kernel_roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)  
    kernel_roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)  

    roberts_x = cv2.filter2D(img, -1, kernel_roberts_x)
    roberts_y = cv2.filter2D(img, -1, kernel_roberts_y)

    roberts_x = cv2.convertScaleAbs(roberts_x)
    roberts_y = cv2.convertScaleAbs(roberts_y)

    roberts_combined = cv2.addWeighted(roberts_x, 0.5, roberts_y, 0.5, 0)

    cv2.imshow('Original Image', img)
    cv2.imshow('Roberts X', roberts_x)
    cv2.imshow('Roberts Y', roberts_y)
    cv2.imshow('Roberts Combined', roberts_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

roberts_edge_detection(r'C:\Users\MONISH\Pictures\images.jpeg')
