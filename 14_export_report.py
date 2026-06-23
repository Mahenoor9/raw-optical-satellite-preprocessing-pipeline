import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load outputs
with rasterio.open("ndvi.tif") as src:
    ndvi = src.read(1)

with rasterio.open("ndvi_change.tif") as src:
    ndvi_change = src.read(1)

with rasterio.open("landcover.tif") as src:
    landcover = src.read(1)

# Save NDVI map
plt.figure(figsize=(8,8))
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI")
plt.title("Final NDVI Map")
plt.axis("off")
plt.savefig("final_ndvi.png")

# Save Change map
plt.figure(figsize=(8,8))
plt.imshow(ndvi_change, cmap="RdYlGn")
plt.colorbar(label="NDVI Change")
plt.title("Vegetation Change Map")
plt.axis("off")
plt.savefig("vegetation_change.png")

# Save Landcover map
plt.figure(figsize=(8,8))
plt.imshow(landcover, cmap="tab10")
plt.colorbar(label="Classes")
plt.title("Landcover Map")
plt.axis("off")
plt.savefig("landcover_map.png")

print("Final report assets exported successfully!")
