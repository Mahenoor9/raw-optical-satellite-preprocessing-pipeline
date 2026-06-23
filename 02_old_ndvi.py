import rasterio
import numpy as np
import math

sun_elevation = 50.44301629
sun_angle_rad = math.radians(sun_elevation)

ref_mult = 0.00002
ref_add = -0.1

with rasterio.open("B4_old.tif") as red_src:
    red = red_src.read(1)
    profile = red_src.profile

with rasterio.open("B5_old.tif") as nir_src:
    nir = nir_src.read(1)

red_reflectance = ((ref_mult * red) + ref_add) / math.sin(sun_angle_rad)
nir_reflectance = ((ref_mult * nir) + ref_add) / math.sin(sun_angle_rad)

ndvi_old = (nir_reflectance - red_reflectance) / (nir_reflectance + red_reflectance)

profile.update(dtype=rasterio.float32)

with rasterio.open("ndvi_old.tif", "w", **profile) as dst:
    dst.write(ndvi_old.astype(rasterio.float32), 1)

print("Old NDVI raster saved!")