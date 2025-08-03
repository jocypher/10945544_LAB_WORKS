import cv2
import os
from matplotlib import pyplot as plt

# Define and create the output subdirectory
output_dir = 'images/processed-2'
os.makedirs(output_dir, exist_ok=True)

# Load the original color image
image_path = 'images/photo.JPG'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

# Convert color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Save converted images
cv2.imwrite(os.path.join(output_dir, 'photo_grayscale.jpg'), gray)
cv2.imwrite(os.path.join(output_dir, 'photo_hsv.jpg'), hsv)
cv2.imwrite(os.path.join(output_dir, 'photo_lab.jpg'), lab)

# Display the images
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)

# Plot and save the grayscale histogram
plt.figure(figsize=(6, 4))
plt.hist(gray.ravel(), bins=256, range=(0, 256))
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

# Save histogram to the same directory
histogram_path = os.path.join(output_dir, 'photo_grayscale_histogram.png')
plt.savefig(histogram_path)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
