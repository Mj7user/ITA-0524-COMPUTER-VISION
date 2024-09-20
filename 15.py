import cv2

def find_contour_coordinates(image_path):
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        for point in contour:
            x, y = point[0]
            print(f"Contour point: ({x}, {y})")
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)  
    cv2.imshow('Image with Contours', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
find_contour_coordinates(r'C:\Users\MONISH\Pictures\images.jpeg')
