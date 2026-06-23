import rasterio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Load bands
with rasterio.open("B2.tif") as src:
    blue = src.read(1).astype(float)

with rasterio.open("B3.tif") as src:
    green = src.read(1).astype(float)

with rasterio.open("B4.tif") as src:
    red = src.read(1).astype(float)
    profile = src.profile

with rasterio.open("B5.tif") as src:
    nir = src.read(1).astype(float)

# Create indices
ndvi = (nir - red) / (nir + red + 1e-10)
ndwi = (green - nir) / (green + nir + 1e-10)
ndbi = (red - nir) / (red + nir + 1e-10)

# Stack features
features = np.stack([blue, green, red, nir, ndvi, ndwi, ndbi], axis=-1)

rows, cols, bands = features.shape
X = features.reshape(rows * cols, bands)

# Create training labels from old landcover map
with rasterio.open("landcover.tif") as src:
    y = src.read(1).flatten()

# Remove invalid pixels
valid_mask = ~np.isnan(X).any(axis=1)
X_valid = X[valid_mask]
y_valid = y[valid_mask]

# Train RF
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_valid, y_valid)

# Predict full image
predictions = rf.predict(X_valid)

# Put back into raster shape
classified = np.zeros(rows * cols)
classified[valid_mask] = predictions
classified = classified.reshape(rows, cols)

# Save output
profile.update(dtype=rasterio.uint8)

with rasterio.open("rf_landcover.tif", "w", **profile) as dst:
    dst.write(classified.astype(rasterio.uint8), 1)

print("Random Forest classification completed!")

# Visualize
plt.figure(figsize=(10,8))
plt.imshow(classified, cmap="tab10")
plt.colorbar(label="RF Classes")
plt.title("Random Forest Landcover Classification")
plt.axis("off")
plt.show()