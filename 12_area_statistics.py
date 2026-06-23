import rasterio
import numpy as np

# Load landcover map
with rasterio.open("landcover.tif") as src:
    landcover = src.read(1)
    pixel_size = src.res[0]   # usually 30m for Landsat

pixel_area_m2 = pixel_size * pixel_size
pixel_area_hectare = pixel_area_m2 / 10000

# Count pixels
water_pixels = np.sum(landcover == 0)
vegetation_pixels = np.sum(landcover == 1)
bare_soil_pixels = np.sum(landcover == 2)
builtup_pixels = np.sum(landcover == 3)

# Convert to hectares
water_area = water_pixels * pixel_area_hectare
vegetation_area = vegetation_pixels * pixel_area_hectare
bare_soil_area = bare_soil_pixels * pixel_area_hectare
builtup_area = builtup_pixels * pixel_area_hectare

print("\nLandcover Area Statistics")
print("--------------------------")
print(f"Water Area: {water_area:.2f} hectares")
print(f"Vegetation Area: {vegetation_area:.2f} hectares")
print(f"Bare Soil Area: {bare_soil_area:.2f} hectares")
print(f"Built-up Area: {builtup_area:.2f} hectares")