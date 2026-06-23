import rasterio
import numpy as np
import matplotlib.pyplot as plt

def estimate_biomass(ndvi_path="ndvi.tif", output_path="biomass.tif", show_plot=True):
    # Open NDVI
    with rasterio.open(ndvi_path) as src:
        ndvi = src.read(1).astype(float)
        profile = src.profile

    # Simple biomass estimation formula
    # Biomass = NDVI × 100 (proxy model)
    biomass = ndvi * 100

    # Remove negatives
    biomass[biomass < 0] = 0

    # Save biomass raster
    profile.update(dtype=rasterio.float32)

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(biomass.astype(rasterio.float32), 1)

    print(f"Biomass raster saved to {output_path}!")

    if show_plot:
        plt.figure(figsize=(10,8))
        plt.imshow(biomass, cmap="YlGn")
        plt.colorbar(label="Biomass Index")
        plt.title("Biomass Estimation")
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    estimate_biomass("ndvi.tif", "biomass.tif", show_plot=True)
