import cv2
from matplotlib import pyplot as plt

# Load image
image = cv2.imread('images/photo.JPG')
cv2.imshow('Original Image', image)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

# Save grayscale image
cv2.imwrite('../images/photo_gray.jpg', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
