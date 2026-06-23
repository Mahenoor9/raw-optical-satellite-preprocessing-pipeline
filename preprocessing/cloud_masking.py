import rasterio
import numpy as np
import matplotlib.pyplot as plt

with rasterio.open("QA_PIXEL.tif") as src:
    qa = src.read(1)

# Basic cloud mask
cloud_mask = (qa & 2720) == 0

plt.figure(figsize=(8,8))
plt.imshow(cloud_mask, cmap='gray')
plt.title("Cloud Mask")
plt.axis("off")
plt.show()