import cv2
import numpy as np
def black_hat_operation(image_path, kernel_size):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image!")
        return

    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    closed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    black_hat_img = cv2.subtract(closed_img, img)
    cv2.imshow('Original Image', img)
    cv2.imshow('Closed Image', closed_img)
    cv2.imshow('Black Hat Image', black_hat_img)
    cv2.imwrite('closed_image.jpg', closed_img)
    cv2.imwrite('black_hat_image.jpg', black_hat_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

black_hat_operation(r'C:\Users\MONISH\Pictures\images.jpeg', 15)
