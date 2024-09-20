import cv2
import matplotlib.pyplot as plt

def plot_histogram(image_path):
    image = cv2.imread(image_path)
    
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    
    for channel, color in zip(channels, colors):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)
    
    plt.xlim([0, 256])
    plt.show()

plot_histogram(r'C:\Users\MONISH\Pictures\images.jpeg')
