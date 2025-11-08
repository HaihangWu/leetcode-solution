import numpy as np
import cv2  # Or use PIL if you're using it for image loading

# Load the image (ensure it's in grayscale or color as needed)
image = cv2.imread(r'C:\Users\hthh1\Downloads\old\depth000000_ADT.png', cv2.IMREAD_GRAYSCALE)  # Load image in grayscale (if you want color, omit cv2.IMREAD_GRAYSCALE)

# Convert to float32 for more precision if needed
image = image.astype(np.float32)

# Get the min and max values
min_val = np.min(image)
max_val = np.max(image)

print(f"Min value: {min_val}")
print(f"Max value: {max_val}")