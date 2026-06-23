# Raw Optical Satellite Preprocessing Pipeline

## Overview
A modular remote sensing pipeline for preprocessing raw Landsat imagery and extracting ecological indicators.

## Pipeline Steps
1. Radiometric correction
2. Atmospheric correction (DOS)
3. NDVI computation
4. Cloud masking
5. Change detection
6. Landcover classification
7. Area statistics
8. Accuracy assessment
9. LST extraction
10. Biomass estimation
11. Temporal vegetation analysis
12. Coregistration RMSE
13. Spectral quality validation

## Tech Stack
- Python
- Rasterio
- NumPy
- Matplotlib
- Scikit-learn
- OpenCV

## Outputs
- NDVI rasters
- Landcover maps
- LST rasters
- Biomass maps
- Temporal vegetation trends

## Results
- Overall Accuracy: 85%
- NDVI Trend:
  - 2018: 0.133
  - 2020: 0.144
  - 2022: 0.147
  - 2024: 0.124
  - 2026: 0.225
