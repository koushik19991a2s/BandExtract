#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import rasterio

# Function to extract and save individual bands
def extract_bands(input_path, output_folder):
    with rasterio.open(input_path) as src:
        for band_idx in range(src.count):
            band_idx += 1  # Bands are indexed starting from 1
            output_path = os.path.join(output_folder, f"band_{band_idx}.tif")
            band_data = src.read(band_idx)
            profile = src.profile
            profile.update(count=1)  # Update the band count in the profile

            with rasterio.open(output_path, "w", **profile) as dst:
                dst.write(band_data, 1)  # Write the band data to the output file

# Example usage
input_path = r"E:/Python_Tutorial/band_extract/hyderabad_tutorial.tif"
output_folder =  r"E:/Python_Tutorial/band_extract/Extracted_bands"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Extract and save individual bands
extract_bands(input_path, output_folder)

