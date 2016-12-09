import cv2
import numpy as np

image_width = 640
image_height = 480
image = np.full([image_height, image_width, 3], [0, 0, 0], np.uint8)

yard = 0.9144

scale_factor = 1.0
length = 105.0
width = 68.0
radius = 9.15
step_size = 0.5
while (scale_factor + step_size) * length < image_width and (scale_factor + step_size) * width < image_height:
    scale_factor += step_size

offset_x = int((image_width - scale_factor * length) / 2)
offset_y = int((image_height - scale_factor * width) / 2)

length = scale_factor * length
width = scale_factor * width
radius = scale_factor * radius

line_colour = (255, 0, 255)

# Touchlines
cv2.line(image, (offset_x, offset_y), (offset_x + int(length), offset_y), line_colour, thickness=1)
cv2.line(image, (offset_x, offset_y + int(width)), (offset_x + int(length), offset_y + int(width)),
         line_colour, thickness=1)

# Goal lines
cv2.line(image, (offset_x, offset_y), (offset_x, offset_y + int(width)), line_colour, thickness=1)
cv2.line(image, (offset_x + int(length), offset_y), (offset_x + int(length), offset_y + int(width)),
         line_colour, thickness=1)

# Half-way line
cv2.line(image, (offset_x + int(length / 2), offset_y), (offset_x + int(length / 2), offset_y + int(width)),
         line_colour,
         thickness=1)

# Center circle
cv2.circle(image, (offset_x + int(length / 2), offset_y + int(width / 2)), int(radius), line_colour, thickness=1)

# Left penalty area
#   Upper line
cv2.line(image, (offset_x, offset_y + int(width / 2 - (4 + 18) * yard * scale_factor)),
         (offset_x + int(18 * yard * scale_factor), offset_y + int(width / 2 - (4 + 18) * yard * scale_factor)),
         line_colour,
         thickness=1)
#   Lower line
cv2.line(image, (offset_x, offset_y + int(width / 2 + (4 + 18) * yard * scale_factor)),
         (offset_x + int(18 * yard * scale_factor), offset_y + int(width / 2 + (4 + 18) * yard * scale_factor)),
         line_colour,
         thickness=1)
# Cross line
cv2.line(image, (offset_x + int(18 * yard * scale_factor), offset_y + int(width / 2 - (4 + 18) * yard * scale_factor)),
         (offset_x + int(18 * yard * scale_factor), offset_y + int(width / 2 + (4 + 18) * yard * scale_factor)),
         line_colour,
         thickness=1)
# Penalty mark
cv2.circle(image, (offset_x + int(12 * yard * scale_factor), offset_y + int(width / 2)), int(0.5 * scale_factor),
           line_colour, thickness=-1)
# Penalty arc
cv2.ellipse(image, (offset_x + int(12 * yard * scale_factor), offset_y + int(width / 2)),
            (int(10 * yard * scale_factor), int(10 * yard * scale_factor)), 180, 128, 232, line_colour, 1)

# Left goal area
#   Upper line
cv2.line(image, (offset_x, offset_y + int(width / 2 - (4 + 6) * yard * scale_factor)),
         (offset_x + int(6 * yard * scale_factor), offset_y + int(width / 2 - (4 + 6) * yard * scale_factor)),
         line_colour,
         thickness=1)
#   Lower line
cv2.line(image, (offset_x, offset_y + int(width / 2 + (4 + 6) * yard * scale_factor)),
         (offset_x + int(6 * yard * scale_factor), offset_y + int(width / 2 + (4 + 6) * yard * scale_factor)),
         line_colour,
         thickness=1)
# Cross line
cv2.line(image, (offset_x + int(6 * yard * scale_factor), offset_y + int(width / 2 - (4 + 6) * yard * scale_factor)),
         (offset_x + int(6 * yard * scale_factor), offset_y + int(width / 2 + (4 + 6) * yard * scale_factor)),
         line_colour,
         thickness=1)

# Right penalty area
#   Upper line
cv2.line(image, (offset_x + int(length), offset_y + int(width / 2 - (4 + 18) * yard * scale_factor)),
         (offset_x + int(length - 18 * yard * scale_factor), offset_y + int(width / 2 - (4 + 18) * yard * scale_factor)),
         line_colour, thickness=1)
#   Lower line
cv2.line(image, (offset_x + int(length), offset_y + int(width / 2 + (4 + 18) * yard * scale_factor)),
         (offset_x + int(length - 18 * yard * scale_factor), offset_y + int(width / 2 + (4 + 18) * yard * scale_factor)),
         line_colour, thickness=1)
# Cross line
cv2.line(image, (offset_x + int(length - 18 * yard * scale_factor), offset_y + int(width / 2 - (4 + 18) * yard * scale_factor)),
         (offset_x + int(length - 18 * yard * scale_factor), offset_y + int(width / 2 + (4 + 18) * yard * scale_factor)),
         line_colour, thickness=1)
# Penalty mark
cv2.circle(image, (offset_x + int(length - 12 * yard * scale_factor), offset_y + int(width / 2)), int(0.5 * scale_factor),
           line_colour, thickness=-1)
# Penalty arc
cv2.ellipse(image, (offset_x + int(length - 12 * yard * scale_factor), offset_y + int(width / 2)),
            (int(10 * yard * scale_factor), int(10 * yard * scale_factor)), 0, 128, 232, line_colour, 1)

# Left goal area
#   Upper line
cv2.line(image, (offset_x + int(length), offset_y + int(width / 2 - (4 + 6) * yard * scale_factor)),
         (offset_x + int(length - 6 * yard * scale_factor), offset_y + int(width / 2 - (4 + 6) * yard * scale_factor)),
         line_colour,
         thickness=1)
#   Lower line
cv2.line(image, (offset_x + int(length), offset_y + int(width / 2 + (4 + 6) * yard * scale_factor)),
         (offset_x + int(length - 6 * yard * scale_factor), offset_y + int(width / 2 + (4 + 6) * yard * scale_factor)),
         line_colour,
         thickness=1)
# Cross line
cv2.line(image, (offset_x + int(length - 6 * yard * scale_factor), offset_y + int(width / 2 - (4 + 6) * yard * scale_factor)),
         (offset_x + int(length - 6 * yard * scale_factor), offset_y + int(width / 2 + (4 + 6) * yard * scale_factor)),
         line_colour,
         thickness=1)

cv2.namedWindow('main')
cv2.imshow('main', image)
cv2.waitKey(0)
