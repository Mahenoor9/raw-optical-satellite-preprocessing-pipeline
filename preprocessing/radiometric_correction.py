import math


# Function to convert DN to Radiance
def dn_to_radiance(dn, mult, add):
    radiance = (mult * dn) + add
    return radiance


# Function to convert DN to Reflectance
def dn_to_reflectance(dn, mult, add, sun_elevation):
    sun_angle_rad = math.radians(sun_elevation)
    reflectance = ((mult * dn) + add) / math.sin(sun_angle_rad)
    return reflectance


# Function to calculate NDVI
def calculate_ndvi(nir, red):
    ndvi = (nir - red) / (nir + red)
    return ndvi


# Sample DN values from GEE
red_dn = 10128
nir_dn = 13529


# Landsat metadata values
sun_elevation = 50.44301629


# Band 4 Radiance metadata
red_rad_mult = 0.010236
red_rad_add = -51.18108

# Band 5 Radiance metadata
nir_rad_mult = 0.0062641
nir_rad_add = -31.32027


# Band 4 Reflectance metadata
red_ref_mult = 0.00002
red_ref_add = -0.1

# Band 5 Reflectance metadata
nir_ref_mult = 0.00002
nir_ref_add = -0.1


# Convert DN to Radiance
red_radiance = dn_to_radiance(
    red_dn,
    red_rad_mult,
    red_rad_add
)

nir_radiance = dn_to_radiance(
    nir_dn,
    nir_rad_mult,
    nir_rad_add
)


# Convert DN to Reflectance
red_reflectance = dn_to_reflectance(
    red_dn,
    red_ref_mult,
    red_ref_add,
    sun_elevation
)

nir_reflectance = dn_to_reflectance(
    nir_dn,
    nir_ref_mult,
    nir_ref_add,
    sun_elevation
)


# Calculate NDVI
ndvi = calculate_ndvi(
    nir_reflectance,
    red_reflectance
)
# Basic vegetation classification
def classify_ndvi(ndvi):
    if ndvi < 0:
        return "Water / Non-vegetation"
    elif ndvi < 0.2:
        return "Sparse vegetation"
    elif ndvi < 0.5:
        return "Moderate vegetation"
    else:
        return "Dense vegetation"


vegetation_type = classify_ndvi(ndvi)

print("Vegetation Type:", vegetation_type)

# Output
print("Red Radiance:", red_radiance)
print("NIR Radiance:", nir_radiance)
print("Red Reflectance:", red_reflectance)
print("NIR Reflectance:", nir_reflectance)
print("NDVI:", ndvi)