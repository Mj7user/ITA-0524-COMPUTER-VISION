import cv2
import numpy as np

def add_watermark(image_path, watermark_text, output_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image!")
        return
    watermarked_img = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (0, 255, 0)  
    font_thickness = 6
    text_size, _ = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)
    
    text_x = watermarked_img.shape[1] - text_size[0] - 10
    text_y = watermarked_img.shape[0] - 10

    cv2.putText(watermarked_img, watermark_text, (text_x, text_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

    cv2.imwrite(output_path, watermarked_img)

    cv2.imshow('Original Image', img)
    cv2.imshow('Watermarked Image', watermarked_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

add_watermark(r'C:\Users\MONISH\Pictures\images.jpeg', 'VK18-MSD7', 'watermarked_image.jpg')
