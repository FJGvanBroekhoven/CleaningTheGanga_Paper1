# README: Python scripts

These Python scripts were utilized for the analysis presented in the article **van Broekhoven et al. (2024) Linking Recharge Water Sources to Groundwater Composition in the Hindon Subbasin of the Ganges River, India** (DOI: https://doi.org/10.1016/j.scitotenv.2024.176399).

## Usage

The scripts should be executed in the following order for proper functionality:
1. **DataPreparation.py**
2. **DataAnalysis.py**
3. **DataVisualisation.py**

## Python Scripts

### DataPreparation.py

This script performs the following tasks:
- Merge datasets (hydrochemistry, isotopes, metadata)
- Adjust values below detection limit (BDL) to half the BDL value
- Remove variables with more than 25% of values below detection limit

### DataAnalysis.py

This script performs the following tasks:
- Log transformation and standardisation of variables
- Factor Analysis with varimax rotation
- Agglomerative Hierarchical Clustering analysis
- Electro-neutrality check
- Plots supplementary figures: S3 and S4

### DataVisualisation.py

This script generates figures and tables presented in the article:
- Figures: 2, 3, 4, and 5 (in PDF format)
- Tables: 1
- Supplementary figures: S1 and S6
- Supplementary table: S1

## Requirements

    Package                       Version
    ----------------------------- ------------
    python                        3.9.12
    numpy                         1.22.3
    pandas                        1.4.2
    geopandas                     0.9.0
    scikit-learn                  1.0.2
    scipy                         1.11.1
    factor-analyzer               0.4.1
    seaborn                       0.12.2
    matplotlib                    3.5.1

For more details or questions, please refer to the main article or contact the corresponding author.

---

When using any material from this repository, please cite as specified in the main article's citation section.
