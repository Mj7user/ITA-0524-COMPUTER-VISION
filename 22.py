import cv2
import numpy as np

def top_hat_operation(image_path, kernel_size):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image!")
        return

    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    top_hat_img = cv2.subtract(img, opened_img)

    cv2.imshow('Original Image', img)
    cv2.imshow('Opened Image', opened_img)
    cv2.imshow('Top Hat Image', top_hat_img)

    cv2.imwrite('opened_image.jpg', opened_img)
    cv2.imwrite('top_hat_image.jpg', top_hat_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

top_hat_operation(r'C:\Users\MONISH\Pictures\images.jpeg', 15)
