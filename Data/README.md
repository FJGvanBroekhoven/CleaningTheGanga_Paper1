# README: Data Directory

This directory contains the data used in the article **van Broekhoven et al. (2024) Linking Recharge Water Sources to Groundwater Composition in the Hindon Subbasin of the Ganges River, India** (DOI: https://doi.org/10.1016/j.scitotenv.2024.176399).

This repository provides the datasets used in the publication of our research article. The data is organized into several CSV files, each corresponding to different aspects of our study. We hope that this data can be useful for other researchers and practitioners in the field. Feel free to explore and analyze the data as needed. If you use this data in your own research, please cite our article.

**Licence**: This dataset is made available under the MIT License. You are free to use, modify, and distribute the data, provided that proper credit is given to the original authors.

**Contact**: For any questions or further information, please contact:
* Frank van Broekhoven [ORCiD](https://orcid.org/0009-0008-1593-9842)
* Email: F.J.G.vanBroekhoven@uu.nl

# Data Files
This directory contains the following files:
* Original: contains the original recieved hydrochemical and isotope data from the National Institute of Hydrology (NIH)
* StartData:
    * Hydrochemical_analysis_NIH_v1.csv
    * Isotope_analysis_NIH_v1.csv
    * Metadata_samples_vanBroekhoven_v1.csv
    * WQ_Hindon_literature_raw_data_v1.csv
    * WQ_Hindon_literature_v2.csv
    * DataForFigures:
        * elevation_profile_v1.csv
        * POIs_along_transect_v2.geojson
        * POI_symbols:
* WorkingData:
    * prepared_dataset_v1.csv (file generated with Python script: DataPreparation.py)
    * analysed_dataset_v1.csv (file generated with Python script: DataAnalysis.py)

## Data-specific information for: Hydrochemical_analysis_NIH_v1.csv
Description: this file contains hydrochemical water quality concentrations for the 53 samples collected during fieldwork in February-March 2023. The lab-analysis was performed by the National Institute of Hydrology (NIH) in Roorkee, India. 
1. Number of variables/columns: 38
2. Number of cases/rows: 53
3. Columns:
    * Sample ID: Identifier for each water sample.
    * pH: pH level of the sample.
    * EC [µS/cm]: Electrical conductivity in microSiemens per centimeter.
    * TDS [mg/L]: Total dissolved solids in milligrams per liter.
    * Hard [mg/L]: Hardness in milligrams per liter.
    * Alk [mg/L]: Alkalinity in milligrams per liter.
    * Cl [mg/L]: Chloride concentration in milligrams per liter.
    * NO3 [mg/L]: Nitrate concentration in milligrams per liter.
    * PO4 [mg/L]: Phosphate concentration in milligrams per liter.
    * SO4 [mg/L]: Sulfate concentration in milligrams per liter.
    * F [mg/L]: Fluoride concentration in milligrams per liter.
    * NO2 [mg/L]: Nitrite concentration in milligrams per liter.
    * Na [mg/L]: Sodium concentration in milligrams per liter.
    * K [mg/L]: Potassium concentration in milligrams per liter.
    * Ca [mg/L]: Calcium concentration in milligrams per liter.
    * Mg [mg/L]: Magnesium concentration in milligrams per liter.
    * NH4 [mg/L]: Ammonium concentration in milligrams per liter.
    * Li [mg/L]: Lithium concentration in milligrams per liter.
    * Silica [mg/L]: Silica concentration in milligrams per liter.
    * COD [mg/L]: Chemical oxygen demand in milligrams per liter.
    * BOD [mg/L]: Biological oxygen demand in milligrams per liter.
    * B [µg/L]: Boron concentration in micrograms per liter.
    * Al [µg/L]: Aluminum concentration in micrograms per liter.
    * V [µg/L]: Vanadium concentration in micrograms per liter.
    * Cr [µg/L]: Chromium concentration in micrograms per liter.
    * Mn [µg/L]: Manganese concentration in micrograms per liter.
    * Fe [µg/L]: Iron concentration in micrograms per liter.
    * Co [µg/L]: Cobalt concentration in micrograms per liter.
    * Ni [µg/L]: Nickel concentration in micrograms per liter.
    * Cu [µg/L]: Copper concentration in micrograms per liter.
    * Zn [µg/L]: Zinc concentration in micrograms per liter.
    * As [µg/L]: Arsenic concentration in micrograms per liter.
    * Se [µg/L]: Selenium concentration in micrograms per liter.
    * Sr [µg/L]: Strontium concentration in micrograms per liter.
    * Cd [µg/L]: Cadmium concentration in micrograms per liter.
    * Ba [µg/L]: Barium concentration in micrograms per liter.
    * Pb [µg/L]: Lead concentration in micrograms per liter.
    * U [µg/L]: Uranium concentration in micrograms per liter.

## Data-specific information for: Hydrochemical_analysis_NIH_v1.csv
Description: this file contains stable isotopic values for H2O for the 53 samples collected during fieldwork in February-March 2023. The lab-analysis was performed by the National Institute of Hydrology (NIH) in Roorkee, India. The analysis was done by Continuous Flow Isotope Ratio Mass Spectrometry and Dual Inlet Isotope Ratio Mass Spectrometry for stable isotopes δ18O and δ2H. The isotopic results are expressed in per mille (‰) relative to Vienna Standard Mean Ocean Water (VSMOW).
1. Number of variables/columns: 3
2. Number of cases/rows: 53
3. Columns:
    * Sample ID: Identifier for each water sample.
    * dO18: stable isotopes δ18O per mille (‰) relative to Vienna Standard Mean Ocean Water (VSMOW).
    * dD: stable isotopes δ2H per mille (‰) relative to Vienna Standard Mean Ocean Water (VSMOW).

## Data-specific information for: Metadata_samples_vanBroekhoven_v1.csv
Description: this file contains stable isotopic values for H2O for the 53 samples collected during fieldwork in February-March 2023. The lab-analysis was performed by the National Institute of Hydrology (NIH) in Roorkee, India. The analysis was done by Continuous Flow Isotope Ratio Mass Spectrometry and Dual Inlet Isotope Ratio Mass Spectrometry for stable isotopes δ18O and δ2H. The isotopic results are expressed in per mille (‰) relative to Vienna Standard Mean Ocean Water (VSMOW).
1. Number of variables/columns: 22
2. Number of cases/rows: 53
3. Columns:
    * Sample ID: Identifier for each water sample.
    * x: Longitude coordinate of the sample location.
    * y: Latitude coordinate of the sample location.
    * CreationDate: Date and time when the sample was collected.
    * Location: Location identifier.
    * depth [feet]: Depth of the water source in feet.
    * depth [m]: Depth of the water source in meters.
    * Elevation surface [mMSL] Hydrosheds: Elevation of the surface in meters above mean sea level, derived from Hydrosheds DEM v.1
    * depth [mMSL]: Depth of the water source in meters above mean sea level.
    * Type of water: Type of water source (e.g., GW for groundwater, SW for surface water).
    * Type: Specific type of water source (e.g., deep tubewell, shallow tubewell, village pond, irrigation canal).
    * Landuse: Land use around the sample location (e.g., agriculture, village, etc).
    * group: Group classification
    * distance startpoint Yamuna [m]: Distance from the starting point to the Yamuna river in meters.
    * distance to canal [m]: Distance to the nearest canal in meters.
    * close to industry: Indication of proximity to industrial areas.
    * EC value [microS/cm]: Electrical conductivity value in microSiemens per centimeter measured in the field.
    * field pH: pH value measured in the field.
    * Temperature: Temperature of the water sample in degrees Celsius.
    * field NO3 [mg/L]: Nitrate concentration in milligrams per liter measured in the field.
    * field NO2 [mg/L]: Nitrite concentration in milligrams per liter measured in the field.
    * Remarks: Additional remarks and observations about the sample.

## Data-specific information for: WQ_Hindon_literature_raw_data_v1.csv
Description: this file contains the retrieved water quality variable values for the Hindon river and its tributaries Kali and Krishni and rainfall from literature. The nearest sample location to our transect has been chosen.
1. Number of variables/columns: 13
2. Number of cases/rows: 210
3. Columns:
    * order: Sequential number indicating the order of the parameter.
    * parameter: Name of the water quality parameter (e.g., pH, EC, BOD).
    * unit: Measurement unit of the parameter (e.g., mg/l).
    * pre monsoon: Value of the parameter before the monsoon season (not provided in this dataset).
    * post monsoon: Value of the parameter after the monsoon season (not provided in this dataset).
    * average: Average value of the parameter based on the available data.
    * based on N samples per location: Number of samples used to calculate the average value.
    * river: Name of the river or rainfall from which the sample was collected (Hindon).
    * sample: Sample identifier used in the original literature source.
    * year(s) data: Year(s) when the data was collected according to the source.
    * source short: Abbreviated citation of the data source
    * source: Full citation of the data source.
    * remarks: Additional remarks and observations.

## Data-specific information for: WQ_Hindon_literature_v2.csv
Description: this file contains the calculated weight average per water quality variable for the Hindon river and its tributaries Kali and Krishni and rainfall from literature.
1. Number of variables/columns: 38
2. Number of cases/rows: 4
3. Columns:
    * Same setup as Hydrochemical_analysis_NIH_v1.csv but transposed

## Data-specific information for: DataForFigures directory
Description: This directory contains files that are used in the ..\Python\DataVisualisation.py Python script to visualise in the crossection: elevation line (elevation_profile_v1.csv), location of the Points of Interest (POIs_along_transect_v2.geojson) and the symbols for the Points of Interest (png files in POI_symbols directory).

## Data-specific information for: WorkingData\prepared_dataset_v1.csv
Description: this file contains the dataset generated with with Python script: ..\Python\DataPreparation.py. See the Python directory and script for more details.

## Data-specific information for: WorkingData\analysed_dataset_v1.csv
Description: this file contains the dataset generated with with Python script: ..\Python\DataAnalysis.py. See the Python directory and script for more details.
