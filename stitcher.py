import cv2
import numpy as np

print(cv2.__version__)
image = cv2.imread('/home/titusz/Pictures/0_frame.png')
out = cv2.normalize(image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
height, width = image.shape[:2]
left_half = image[0:height, 0:int(width/2)]
upper_half = image[0:int(height/2), 0:width]
cv2.namedWindow('whole')
cv2.namedWindow('left_half')
cv2.namedWindow('bottom_half')
cv2.imshow('left_half', left_half)
cv2.imshow('bottom_half', upper_half)

stitcher = cv2.createStitcher(False)
cv2.ocl.setUseOpenCL(False)
whole = stitcher.stitch((left_half, upper_half))

cv2.imshow('whole', whole)
cv2.waitKey(0)
