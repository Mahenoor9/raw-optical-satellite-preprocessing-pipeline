from sklearn.metrics import classification_report, confusion_matrix
import rasterio
import numpy as np

# Load old labels
with rasterio.open("landcover.tif") as src:
    y_true = src.read(1).flatten()

# Load RF predictions
with rasterio.open("rf_landcover.tif") as src:
    y_pred = src.read(1).flatten()

# Remove invalid
valid = ~np.isnan(y_true) & ~np.isnan(y_pred)

y_true = y_true[valid]
y_pred = y_pred[valid]

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)

print("Confusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_true, y_pred))