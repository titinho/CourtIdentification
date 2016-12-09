import cv2

image = cv2.imread('/home/titusz/Pictures/dort_frei_frames/466_frame.png')
hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
hue, lightness, saturation = cv2.split(hls_image)
mask = cv2.inRange(lightness, 128, 255)
image = cv2.bitwise_and(image, image, mask=mask)
cv2.namedWindow('main')
cv2.imshow('main', image)
cv2.waitKey(0)
