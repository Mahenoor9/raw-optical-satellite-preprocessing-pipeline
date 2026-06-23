import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load OLD NDVI
with rasterio.open("ndvi_old.tif") as src1:
    ndvi_old = src1.read(1)

# Load NEW NDVI + profile INSIDE block
with rasterio.open("ndvi.tif") as src2:
    ndvi_new = src2.read(1)
    profile = src2.profile

# Change Detection
ndvi_change = ndvi_new - ndvi_old

# Save result
profile.update(dtype=rasterio.float32)

with rasterio.open("ndvi_change.tif", "w", **profile) as dst:
    dst.write(ndvi_change.astype(rasterio.float32), 1)

print("NDVI change raster saved!")

# Visualize
plt.figure(figsize=(10, 8))
plt.imshow(ndvi_change, cmap="RdYlGn")
plt.colorbar(label="NDVI Change")
plt.title("Vegetation Change Detection")
plt.axis("off")
plt.show()