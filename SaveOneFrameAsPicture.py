import cv2
import numpy as np


cap = cv2.VideoCapture('D:/Training Image Processing/Parking Project/parking5.mp4')

ret , frame = cap.read()
cv2.imwrite('D:/Training Image Processing/Parking Project/parking5.jpg',frame)
