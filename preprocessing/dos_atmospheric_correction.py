import rasterio
import numpy as np

def dos_correction(input_band="B4.tif", output_band="red_dos.tif"):
    with rasterio.open(input_band) as src:
        red = src.read(1).astype(float)
        profile = src.profile

    dark_pixel = np.min(red)
    corrected_red = red - dark_pixel
    corrected_red[corrected_red < 0] = 0

    profile.update(dtype=rasterio.float32)

    with rasterio.open(output_band, "w", **profile) as dst:
        dst.write(corrected_red.astype(rasterio.float32), 1)

    print(f"DOS corrected red band saved to {output_band}!")

if __name__ == "__main__":
    dos_correction("B4.tif", "red_dos.tif")
