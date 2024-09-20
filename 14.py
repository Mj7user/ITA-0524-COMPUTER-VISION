import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('BGR Palette')

cv2.createTrackbar('B', 'BGR Palette', 0, 255, nothing)
cv2.createTrackbar('G', 'BGR Palette', 0, 255, nothing)
cv2.createTrackbar('R', 'BGR Palette', 0, 255, nothing)

image = np.zeros((300, 512, 3), np.uint8)

while True:
  
    b = cv2.getTrackbarPos('B', 'BGR Palette')
    g = cv2.getTrackbarPos('G', 'BGR Palette')
    r = cv2.getTrackbarPos('R', 'BGR Palette')
    
    image[:] = [b, g, r]
    
    cv2.imshow('BGR Palette', image)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
