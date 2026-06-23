import rasterio
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score

# Load classification
with rasterio.open("landcover.tif") as src:
    classified = src.read(1)

# Simulated ground truth samples (replace later with actual field points)
np.random.seed(42)

sample_rows = np.random.randint(0, classified.shape[0], 100)
sample_cols = np.random.randint(0, classified.shape[1], 100)

predicted = classified[sample_rows, sample_cols]

# Fake ground truth (for demo)
ground_truth = predicted.copy()

# Introduce small error
error_indices = np.random.choice(len(ground_truth), 15)
ground_truth[error_indices] = (ground_truth[error_indices] + 1) % 4

# Metrics
cm = confusion_matrix(ground_truth, predicted)
acc = accuracy_score(ground_truth, predicted)

print("\nConfusion Matrix:")
print(cm)

print(f"\nOverall Accuracy: {acc*100:.2f}%")