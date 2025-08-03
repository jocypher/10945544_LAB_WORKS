import cv2
import os
from matplotlib import pyplot as plt

# Ensure the output directory exists
output_dir = '../images'
os.makedirs(output_dir, exist_ok=True)

# Load color image
image = cv2.imread('images/photo.JPG')  # Adjust if needed
if image is None:
    raise FileNotFoundError("Image not found. Make sure 'images/photo.JPG' exists.")

# Convert color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Save converted images
cv2.imwrite(f'{output_dir}/photo_grayscale.jpg', gray)
cv2.imwrite(f'{output_dir}/photo_hsv.jpg', hsv)
cv2.imwrite(f'{output_dir}/photo_lab.jpg', lab)

# Display images
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)

# Plot grayscale histogram
plt.figure(figsize=(6, 4))
plt.hist(gray.ravel(), bins=256, range=(0, 256))
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.savefig(f'{output_dir}/photo_grayscale_histogram.png')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
