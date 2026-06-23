import rasterio
import numpy as np
import math

def calculate_ndvi(red_path="B4.tif", nir_path="B5.tif", output_path="ndvi.tif"):
    # Landsat metadata
    sun_elevation = 50.44301629
    sun_angle_rad = math.radians(sun_elevation)

    ref_mult = 0.00002
    ref_add = -0.1

    with rasterio.open(red_path) as red_src:
        red = red_src.read(1)
        profile = red_src.profile

    with rasterio.open(nir_path) as nir_src:
        nir = nir_src.read(1)

    # Convert DN to Reflectance
    red_reflectance = ((ref_mult * red) + ref_add) / np.sin(sun_angle_rad)
    nir_reflectance = ((ref_mult * nir) + ref_add) / np.sin(sun_angle_rad)

    # Compute NDVI
    ndvi = (nir_reflectance - red_reflectance) / (
        nir_reflectance + red_reflectance + 1e-10
    )

    # Save NDVI output
    profile.update(dtype=rasterio.float32)

    with rasterio.open(output_path, "w", **profile) as dst:
        dst.write(ndvi.astype(rasterio.float32), 1)

    print(f"NDVI raster saved successfully to {output_path}!")
    return ndvi

if __name__ == "__main__":
    calculate_ndvi("B4.tif", "B5.tif", "ndvi.tif")
