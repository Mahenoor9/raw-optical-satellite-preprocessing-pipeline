import rasterio
import numpy as np
import matplotlib.pyplot as plt

def extract_lst(thermal_path="B10.tif", output_path="lst.tif", show_plot=True):
    # Open thermal band (Band 10)
    with rasterio.open(thermal_path) as src:
        thermal = src.read(1).astype(float)
        profile = src.profile

    # Landsat 8 constants
    ML = 0.0003342
    AL = 0.1
    K1 = 774.8853
    K2 = 1321.0789

    # Step 1: DN to Radiance
    radiance = (ML * thermal) + AL

    # Step 2: Radiance to Brightness Temperature
    bt = K2 / np.log((K1 / radiance) + 1)

    # Convert Kelvin to Celsius
    lst = bt - 273.15

    # Save
    profile.update(dtype=rasterio.float32)

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(lst.astype(rasterio.float32), 1)

    print(f"LST raster saved to {output_path}!")

    if show_plot:
        plt.figure(figsize=(10,8))
        plt.imshow(lst, cmap="hot")
        plt.colorbar(label="Temperature (°C)")
        plt.title("Land Surface Temperature")
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    extract_lst("B10.tif", "lst.tif", show_plot=True)
