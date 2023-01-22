import sys
sys.path.append("C:\\Users\\AJ Matise\\AppData\\Local\\Programs\\Python\\Python311")

print("This is the system path")
print(sys.path)
print("End system path")
print("---------------")

import numpy

print("END NUMPY IMPORT")
print("----------------")

from cv2 import cv2

image1 = cv2.imread("C:\\Users\\AJ Matise\\Desktop\\image1.png")
image2 = cv2.imread("C:\\Users\\AJ Matise\\Desktop\\image2.png")

def image_overlay(image1, image2, location):
    h, w = image1.shape[:2]
    h1, w1 = image2.shape[:2]
    x, y = location
    image1[y:y+h1, x:x+w1] = image2
    return image1 

#if __name__ == "__main__":

image1 = cv2.imread("C:/Users/AJ Matise/Desktop/image1.png")
image2 = cv2.imread("C:/Users/AJ Matise/Desktop/image2.png")
image_to_display = image_overlay(image1, image2, location = (100,100))
cv2.imshow('image_to_display', image_to_display)
cv2.waitKey(0)
