from preprocessing.dos_atmospheric_correction import dos_correction
from indices.ndvi import calculate_ndvi
from classification.landcover_classification import rule_based_classification
from thermal.lst_extraction import extract_lst
from biomass.biomass_estimation import estimate_biomass
from temporal.temporal_stack_analysis import temporal_trend

print("Starting Raw Optical Satellite Pipeline...")

# Step 1: Atmospheric correction
dos_correction("B4.tif", "red_corrected.tif")

# Step 2: NDVI
ndvi = calculate_ndvi("B4.tif", "B5.tif", "outputs/ndvi.tif")

# Step 3: Rule-based landcover
rule_based_classification("outputs/ndvi.tif", "outputs/landcover.tif", show_plot=False)

# Step 4: Land Surface Temperature
extract_lst("B10.tif", "outputs/lst.tif", show_plot=False)

# Step 5: Biomass estimation
estimate_biomass("outputs/ndvi.tif", "outputs/biomass.tif", show_plot=False)

# Step 6: Temporal trend
temporal_trend([
    "ndvi_2018.tif",
    "ndvi_2020.tif",
    "ndvi_2022.tif",
    "ndvi_2024.tif",
    "outputs/ndvi.tif"
], show_plot=False)

print("Pipeline finished successfully!")