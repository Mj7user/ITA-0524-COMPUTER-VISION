import cv2

def modify_roi(image_path):
    
    image = cv2.imread(image_path)
    
    x, y, width, height = 50, 50, 100, 100 
    roi = image[y:y+height, x:x+width]
    
    image[y:y+height, x:x+width] = (0, 255, 0)  
    
    cv2.imshow('Modified Image', image)
    
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
modify_roi(r'C:\Users\MONISH\Pictures\images.jpeg')
