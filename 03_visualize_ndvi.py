import rasterio
import matplotlib.pyplot as plt

with rasterio.open("ndvi.tif") as src:
    ndvi = src.read(1)

plt.figure(figsize=(8,8))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label="NDVI")
plt.title("NDVI Map - Ballari")
plt.show()