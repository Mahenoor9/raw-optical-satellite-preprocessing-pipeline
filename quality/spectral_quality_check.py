import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Original Red band
with rasterio.open("B4.tif") as src:
    original = src.read(1).astype(float)

# Py6S corrected / Brovey output
with rasterio.open("red_dos.tif") as src:
    corrected = src.read(1).astype(float)

# Flatten arrays
original_flat = original.flatten()
corrected_flat = corrected.flatten()

# Remove invalid values
mask = (~np.isnan(original_flat)) & (~np.isnan(corrected_flat))

original_flat = original_flat[mask]
corrected_flat = corrected_flat[mask]

# Correlation
correlation = np.corrcoef(original_flat, corrected_flat)[0, 1]

print(f"Spectral Correlation: {correlation:.4f}")

# Plot scatter
plt.figure(figsize=(8,8))
plt.scatter(original_flat[:5000], corrected_flat[:5000], alpha=0.3)
plt.xlabel("Original Band Values")
plt.ylabel("Corrected Band Values")
plt.title("Spectral Quality Check")
plt.grid(True)
plt.show()