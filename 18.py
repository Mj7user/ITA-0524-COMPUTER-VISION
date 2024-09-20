import cv2
import numpy as np
def prewitt_edge_detection(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Error: Could not load image!")
        return

    kernel_prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)  
    kernel_prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)  

    prewitt_x = cv2.filter2D(img, cv2.CV_64F, kernel_prewitt_x)
    prewitt_y = cv2.filter2D(img, cv2.CV_64F, kernel_prewitt_y)

    prewitt_x = cv2.convertScaleAbs(prewitt_x)
    prewitt_y = cv2.convertScaleAbs(prewitt_y)

    prewitt_combined = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

    cv2.imshow('Original Image', img)
    cv2.imshow('Prewitt X', prewitt_x)
    cv2.imshow('Prewitt Y', prewitt_y)
    cv2.imshow('Prewitt Combined', prewitt_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

prewitt_edge_detection(r'C:\Users\MONISH\Pictures\images.jpeg')
