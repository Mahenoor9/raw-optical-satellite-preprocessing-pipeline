import rasterio
import numpy as np
import matplotlib.pyplot as plt

with rasterio.open("ndvi.tif") as ndvi_src:
    ndvi = ndvi_src.read(1)
    profile = ndvi_src.profile

with rasterio.open("QA_PIXEL.tif") as qa_src:
    qa = qa_src.read(1)

cloud_mask = (qa & 2720) == 0

masked_ndvi = np.where(cloud_mask, ndvi, np.nan)

profile.update(dtype=rasterio.float32)

with rasterio.open("ndvi_masked.tif", "w", **profile) as dst:
    dst.write(masked_ndvi.astype(rasterio.float32), 1)

plt.figure(figsize=(8,8))
plt.imshow(masked_ndvi, cmap="RdYlGn")
plt.title("Cloud Masked NDVI")
plt.colorbar()
plt.axis("off")
plt.show()

print("Cloud-masked NDVI saved.")