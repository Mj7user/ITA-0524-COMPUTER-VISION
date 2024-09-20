import cv2

def apply_adaptive_thresholding(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Error: Could not load image!")
        return

    binary_img_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 11, 2)
    
    binary_img_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    cv2.imshow('Original Image', img)
    cv2.imshow('Adaptive Thresholding - Gaussian', binary_img_gaussian)
    cv2.imshow('Adaptive Thresholding - Mean', binary_img_mean)

    cv2.imwrite('adaptive_threshold_gaussian.jpg', binary_img_gaussian)
    cv2.imwrite('adaptive_threshold_mean.jpg', binary_img_mean)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

apply_adaptive_thresholding(r'C:\Users\MONISH\Pictures\images.jpeg', 'output_path')
