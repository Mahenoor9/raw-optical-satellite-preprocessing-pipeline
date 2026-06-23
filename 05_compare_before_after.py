import rasterio
import matplotlib.pyplot as plt

with rasterio.open("B4.tif") as src:
    original = src.read(1)

with rasterio.open("red_dos.tif") as src:
    corrected = src.read(1)

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(original, cmap='gray')
plt.title("Original Red Band")

plt.subplot(1,2,2)
plt.imshow(corrected, cmap='gray')
plt.title("DOS Corrected Red Band")

plt.show()