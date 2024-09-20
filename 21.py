import cv2

def crop_copy_paste_roi(source_image_path, target_image_path, roi_start_x, roi_start_y, roi_width, roi_height, paste_x, paste_y):
    source_img = cv2.imread(source_image_path)
    
    if source_img is None:
        print("Error: Could not load source image!")
        return

    roi = source_img[roi_start_y:roi_start_y + roi_height, roi_start_x:roi_start_x + roi_width]

    target_img = cv2.imread(target_image_path)
    
    if target_img is None:
        print("Error: Could not load target image!")
        return

    if (paste_y + roi_height > target_img.shape[0]) or (paste_x + roi_width > target_img.shape[1]):
        print("Error: The ROI does not fit in the target image at the specified location!")
        return

    target_img[paste_y:paste_y + roi_height, paste_x:paste_x + roi_width] = roi

    cv2.imshow('Source Image', source_img)
    cv2.imshow('Target Image with ROI Pasted', target_img)

    cv2.imwrite('result_image.jpg', target_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

crop_copy_paste_roi(r'C:\Users\MONISH\Pictures\images.jpeg', r'C:\Users\MONISH\Pictures\IMG_20201224_193559_947.jpg', 50, 50, 100, 100, 200, 200)
