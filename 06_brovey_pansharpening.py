import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load bands
with rasterio.open("B2.tif") as blue_src:
    blue = blue_src.read(1).astype(float)

with rasterio.open("B3.tif") as green_src:
    green = green_src.read(1).astype(float)

with rasterio.open("B4.tif") as red_src:
    red = red_src.read(1).astype(float)
    profile = red_src.profile

with rasterio.open("B8.tif") as pan_src:
    pan = pan_src.read(
        1,
        out_shape=(red.shape[0], red.shape[1])  # resize PAN to RGB size
    ).astype(float)

# Avoid divide-by-zero
rgb_sum = red + green + blue
rgb_sum[rgb_sum == 0] = 1

# Brovey transform
red_brovey = (red / rgb_sum) * pan
green_brovey = (green / rgb_sum) * pan
blue_brovey = (blue / rgb_sum) * pan

# Stack into RGB image
brovey = np.stack([red_brovey, green_brovey, blue_brovey], axis=-1)

# Normalize for visualization
brovey_norm = (brovey - brovey.min()) / (brovey.max() - brovey.min())

# Display
plt.figure(figsize=(8,8))
plt.imshow(brovey_norm)
plt.title("Brovey Pansharpened Image")
plt.axis("off")
plt.show()