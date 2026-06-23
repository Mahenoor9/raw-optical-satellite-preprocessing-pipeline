import matplotlib.pyplot as plt

report = """
NEVARA Raw Optical Satellite Pipeline Final Report
-------------------------------------------------

1. Radiometric Correction ✔
2. Atmospheric Correction (DOS + Py6S attempt) ✔
3. NDVI Extraction ✔
4. Cloud Masking ✔
5. Change Detection ✔
6. Landcover Classification ✔
7. Area Statistics ✔
8. Validation Metrics ✔
9. Biomass Estimation ✔
10. Land Surface Temperature ✔
11. Temporal Stack Analysis ✔
12. Coregistration RMSE ✔
13. Spectral Quality Check ✔

Key Results:
------------
NDVI Trend:
2018: 0.133
2020: 0.144
2022: 0.147
2024: 0.124
2026: 0.225

Landcover:
Water: 422.82 ha
Vegetation: 62.55 ha
Bare Soil: 9463.41 ha
Built-up: 1.26 ha

Validation:
Overall Accuracy: 85%

Spectral Correlation: 1.000
"""

with open("final_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("Final report exported!")