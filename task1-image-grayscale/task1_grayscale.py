import cv2
from matplotlib import pyplot as plt

import os
import cv2

# Load image
image = cv2.imread('images/photo.JPG')
cv2.imshow('Original Image', image)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

# Define subdirectory path
output_dir = 'images/processed'
output_path = os.path.join(output_dir, 'photo_gray.jpg')

# Create the subdirectory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save grayscale image
cv2.imwrite(output_path, gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

