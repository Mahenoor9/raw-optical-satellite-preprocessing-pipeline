from Py6S import *
import rasterio
import numpy as np

# Open Red band
with rasterio.open("B4.tif") as src:
    red = src.read(1).astype(float)
    profile = src.profile

# Setup Py6S model
s = SixS()

# Atmosphere settings
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.Tropical)
s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Continental)

# Geometry
s.geometry = Geometry.User()
s.geometry.solar_z = 39.56   # 90 - sun elevation (50.44)
s.geometry.solar_a = 133.72
s.geometry.view_z = 0
s.geometry.view_a = 0

# Wavelength (Band 4 = Red)
s.wavelength = Wavelength(PredefinedWavelengths.LANDSAT_OLI_B4)

# Run model
s.run()

# Extract atmospheric correction values
xa = s.outputs.coef_xa
xb = s.outputs.coef_xb
xc = s.outputs.coef_xc

# Convert DN -> TOA Reflectance (same as before)
ref_mult = 0.00002
ref_add = -0.1

toa = (red * ref_mult) + ref_add

# Apply 6S correction
y = xa * toa - xb
surface_reflectance = y / (1 + xc * y)

# Remove negatives
surface_reflectance[surface_reflectance < 0] = 0

# Save corrected image
profile.update(dtype=rasterio.float32)

with rasterio.open("B4_py6s_corrected.tif", "w", **profile) as dst:
    dst.write(surface_reflectance.astype(rasterio.float32), 1)

print("Py6S atmospheric correction completed!")