# BandExtract

BandExtract is written in python and used to extract individual band from stacked satellite image and save it to the individual tiff image.

## Prerequisites

Before running this code in your system you have to install `os` and `rasterio` library in your system. You can see the installition process of  `os` library [here](https://anaconda.org/jmcmurray/os). Geographic information systems use GeoTIFF and other formats to organize and store gridded raster datasets such as satellite imagery and terrain models. `rasterio` reads and writes these formats and provides a Python API based on `Numpy` N-dimensional arrays and `GeoJSON`. To install the `rasterio`, [clik here.](https://rasterio.readthedocs.io/en/stable/installation.html)

# BandExtract
Now we will breakdown and see how to execute the code: 

```bash
import os
import rasterio
```
These are import statements. These lines import the necessary modules for the code: `os` for working with the operating system, and `rasterio` for working with raster data.
```bash
def extract_bands(input_path, output_folder):
```
This line defines a function called `extract_bands` that takes two parameters: `input_path` (the path to the stacked image file) and `output_folder` (the folder where individual bands will be saved).

```bash
    with rasterio.open(input_path) as src:
```
The line used to opens the stacked image file specified by `input_path` using `rasterio.open()`. The file is opened in a context manager, which ensures that it is properly closed after use.

 ```bash
        for band_idx in range(src.count):
            band_idx += 1 
```
After opening the stacked image, it will set up a loop that iterates over the number of bands in the image (obtained using `src.count`). The `band_idx` variable is used to keep track of the current band index, and `band_idx += 1` increments the index by 1 since bands are typically indexed starting from 1 instead of 0.

 ```bash
          output_path = os.path.join(output_folder, f"band_{band_idx}.tif")
```
Completing the loop operation then it constructs the output path for the current band by using `os.path.join()` to combine `output_folder` and the band-specific filename, which follows the pattern `"band_{band_idx}.tif"`.

```bash
            band_data = src.read(band_idx)
```
This line reads the data for the current band using `src.read(band_idx)`. The `band_idx` specifies the index of the band to be read.

```bash
            profile = src.profile
            profile.update(count=1)
```
After reading indexes of bands it store the metadata (profile) of the input image in the profile variable. The `profile.update(count=1)` line updates the band count in the profile to 1 since we are writing each band individually.

```bash
            with rasterio.open(output_path, "w", **profile) as dst:
                dst.write(band_data, 1)
```
These lines open the output file specified by `output_path` using `rasterio.open()` with mode `"w"` (write). The `**profile` syntax passes the profile metadata to the output file. Within the context manager, `dst.write(band_data, 1)` writes the band data to the output file, where the `1` specifies the band index.

```bash
input_path = "path/to/stacked_image.tif"
output_folder = "path/to/output_folder"

os.makedirs(output_folder, exist_ok=True)

extract_bands(input_path, output_folder)
```
These lines provide an example usage of the `extract_bands` function. The `input_path` variable is set to the path of the stacked image file, and the `output_folder` variable is set to the desired output folder. Then, `os.makedirs(output_folder, exist_ok=True)` creates the output folder if it doesn't already exist. Finally, `extract_bands(input_path, output_folder)` is called to perform the extraction and saving of individual bands.

**Here is the full code:**
```bash
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
input_path = "path/to/stacked_image.tif"
output_folder = "path/to/output_folder"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Extract and save individual bands
extract_bands(input_path, output_folder)
```


# Benefit of using BandExtract

Extracting bands from stacked satellite images can offer several benefits in various applications. Here are some advantages:

1. **Feature Analysis**: Extracting specific bands allows you to isolate and analyze different features of interest. For example, if you're interested in vegetation analysis, you can extract the near-infrared (NIR) band, which is sensitive to vegetation health and can help assess vegetation density and vigor.

2. **Data Reduction**: Stacked satellite images often consist of multiple bands with different spectral information. Extracting specific bands can help reduce the data volume while retaining the relevant information for your analysis. This can be particularly useful when dealing with large datasets or limited computational resources.

3. **Customized Analysis**: Different bands capture specific information about the Earth's surface, such as vegetation, water bodies, urban areas, or geological features. By extracting bands relevant to your analysis, you can customize your analysis based on the specific information you require.

4. **Enhanced Visualization**: Extracting bands can enhance the visualization of certain features. For example, using the shortwave infrared (SWIR) band can help identify and map geological structures or mineral deposits that might not be visible in other bands.

5. **Data Fusion**: Extracted bands from different satellite sensors or platforms can be fused together to create composite images, incorporating the advantages of each band. This can lead to more accurate and comprehensive analysis by combining the strengths of different sensors.

6. **Data Integration**: Extracted bands can be combined with other geospatial datasets, such as topographic data or climate data, to gain a more comprehensive understanding of the studied area. This integration can provide valuable insights for applications like land-use planning, environmental monitoring, or disaster management.

7. **Machine Learning Applications**: Extracted bands can serve as input features for machine learning algorithms, enabling the development of predictive models. Machine learning models can utilize the spectral information from different bands to classify land cover, predict crop yields, or detect anomalies.

8. **Change Detection**: By comparing extracted bands from different time periods, you can identify changes in the landscape, such as urban expansion, deforestation, or land degradation. Change detection analysis can be valuable for monitoring environmental changes and supporting decision-making processes.

It's important to note that the specific benefits of band extraction can vary depending on the application, the satellite imagery used, and the desired analysis objectives.

## Contact ME
* Email: koushikghosh1a2s@gmail.com.

* LinkedIn: [Koushik Ghosh](https://www.linkedin.com/in/koushik-ghosh-490761192/)

* ResearchGate: [Koushik Ghosh](https://www.researchgate.net/profile/Koushik-Ghosh-23)



