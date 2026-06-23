import rasterio
import numpy as np
import matplotlib.pyplot as plt

def rule_based_classification(ndvi_path="ndvi.tif", output_path="landcover.tif", show_plot=True):
    # Load bands
    with rasterio.open("B2.tif") as blue_src:
        blue = blue_src.read(1).astype(float)

    with rasterio.open("B3.tif") as green_src:
        green = green_src.read(1).astype(float)

    with rasterio.open("B4.tif") as red_src:
        red = red_src.read(1).astype(float)
        profile = red_src.profile

    with rasterio.open("B5.tif") as nir_src:
        nir = nir_src.read(1).astype(float)

    # Load ndvi from ndvi_path if it exists
    try:
        with rasterio.open(ndvi_path) as ndvi_src:
            ndvi = ndvi_src.read(1).astype(float)
    except Exception:
        ndvi = (nir - red) / (nir + red + 1e-10)

    ndwi = (green - nir) / (green + nir + 1e-10)
    ndbi = (red - nir) / (red + nir + 1e-10)

    # Create landcover array
    landcover = np.zeros_like(ndvi)

    # Rules
    landcover[ndwi > 0.1] = 0          # Water
    landcover[ndvi > 0.3] = 1          # Vegetation
    landcover[(ndvi < 0.2) & (ndbi < 0)] = 2   # Bare Soil
    landcover[ndbi > 0.05] = 3         # Built-up

    # Save raster
    profile.update(dtype=rasterio.uint8)

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(landcover.astype(rasterio.uint8), 1)

    print(f"Landcover classification saved to {output_path}!")

    if show_plot:
        plt.figure(figsize=(10,8))
        plt.imshow(landcover, cmap="tab10")
        plt.colorbar(label="Landcover Classes")
        plt.title("Landcover Classification")
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    rule_based_classification("ndvi.tif", "landcover.tif", show_plot=True)
