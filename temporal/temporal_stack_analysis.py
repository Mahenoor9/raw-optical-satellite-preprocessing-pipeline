import rasterio
import numpy as np
import matplotlib.pyplot as plt
import re

def temporal_trend(files=None, show_plot=True):
    if files is None:
        files = {
            "2018": "ndvi_2018.tif",
            "2020": "ndvi_2020.tif",
            "2022": "ndvi_2022.tif",
            "2024": "ndvi_2024.tif",
            "2026": "ndvi.tif"
        }

    # If list is passed, transform it into a dictionary by parsing years
    if isinstance(files, list):
        file_dict = {}
        for f in files:
            match = re.search(r'\d{4}', f)
            if match:
                file_dict[match.group(0)] = f
            else:
                if "ndvi.tif" in f:
                    file_dict["2026"] = f
                else:
                    file_dict[str(2018 + len(file_dict)*2)] = f
        files = file_dict

    years = []
    mean_ndvi = []

    for year, file in files.items():
        with rasterio.open(file) as src:
            ndvi = src.read(1).astype(float)
            ndvi = ndvi[~np.isnan(ndvi)]
            mean_value = np.mean(ndvi)

            years.append(int(year))
            mean_ndvi.append(mean_value)

    print("Temporal NDVI Trend:")
    for y, v in zip(years, mean_ndvi):
        print(f"{y}: {v:.3f}")

    if show_plot:
        plt.figure(figsize=(10,6))
        plt.plot(years, mean_ndvi, marker='o')
        plt.xlabel("Year")
        plt.ylabel("Mean NDVI")
        plt.title("Temporal Vegetation Trend")
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    temporal_trend(None, show_plot=True)
