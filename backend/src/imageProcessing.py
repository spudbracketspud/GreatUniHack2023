import cv2
import numpy as np

def process(path):
    try:
        image = cv2.imread(path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_green = np.array([35, 50, 50])
        upper_green = np.array([85, 255, 255])

        green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
        green_areas = cv2.bitwise_and(image, image, mask=green_mask)
        green_pixel_count = np.count_nonzero(green_mask)
        total_pixel_count = green_mask.size
        green_percentage = (green_pixel_count / total_pixel_count) * 100
    except:
        return -1
    return green_percentage

