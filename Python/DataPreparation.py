# -*- coding: utf-8 -*-
"""
Title: "DataPreparation"
Author: "Frank van Broekhoven"
ORCiD: https://orcid.org/0009-0008-1593-9842
Date: '2024-06-24'
General info:
    
    This script is part of the article
    - vanBroekhoven et al.(2024) Linking recharge water sources to groundwater composition in the Hindon subbasin of the Ganges River, India.
    
    This script is used for:
    - merge datasets (hydrochemistry + isotopes + metadata)
    - change below detection limit (BDL) values to half the DBL value
    - drop variables with >25% of the values BDL

"""
#%% import modules
import pandas as pd
import os

#%% read datasets and combine

# set directory paths
repo_dir = r'C:\GitHub\Temp_CleaningTheGanga_Paper1' # change this to the location where you stored the reposiotry
datadir = os.path.join(repo_dir, r'Data\StartData')

# read metadata collected (ground)water samples
path_meta = os.path.join(datadir, 'Metadata_samples_vanBroekhoven_v1.csv')
df_meta = pd.read_csv(path_meta, delimiter=(';'), index_col=('Sample ID'))
df = df_meta.copy()

# read hydrochemistry data NIH
path_hydrochem = os.path.join(datadir, 'Hydrochemical_analysis_NIH_v1.csv')
df_hydrochem = pd.read_csv(path_hydrochem, delimiter=(';'), index_col=('Sample ID'), encoding="ISO-8859-1")
df = pd.concat([df, df_hydrochem], axis=1)

# read isotope data NIH
path_isotope = os.path.join(datadir, 'Isotope_analysis_NIH_v1.csv')
df_isotope = pd.read_csv(path_isotope, delimiter=(';'), index_col=('Sample ID'), encoding="ISO-8859-1")
df = pd.concat([df, df_isotope], axis=1)


#%% hydrochemical dataset alterations

# set below detectable limit measurement to half values BDL value (done for NO2, NH4, Ni, Se and NO3)
df['NO2 [mg/L]'] = df['NO2 [mg/L]'].replace('ND', 0.005).astype(float) # detection limit = 0.01 mg/L. there are 10 values below detection limit: F11.1, 11.2, 13.2, 14.1, 14.2, 14.3. 15.3. 16.1, 16.3 and 17.1
df['NH4 [mg/L]'] = df['NH4 [mg/L]'].replace('ND', 0.025).astype(float) # detection limit = 0.05 mg/L. there were 2 values below detection limit: F11.1 and F17.3
df['Ni [µg/L]'] = df['Ni [µg/L]'].replace('<0.000', 0.005).astype(float) # lowest value in dataset is 0.011725. i assumed 0.01 as detection limit. there were 2 values below detection limit: F14.1 and F16.1    
df['Se [µg/L]'] = df['Se [µg/L]'].replace('<0.000', 0.005).astype(float) # lowest value in dataset is 0.0334. i assumed 0.01 as detection limit. there are 3 values below detection limit: F9.3, F9.4 and F2.5
df['NO3 [mg/L]'] = df['NO3 [mg/L]'].replace(0, 0.0005).astype(float) # Sample F8.4 has 0.000 mg/L NO3. i assumed 0.001 as detection limit.

# remove variables where 25% of the samples are below detectable limit (PO4, Li, BOD removed)
df = df.drop(['PO4 [mg/L]', 'Li [mg/L]', 'BOD [mg/L]'], axis=1)

# correct Field EC value of F4.1 and Lab EC of F9.1 and F2.1
# The field and lab measurements were crosschecked and these three values didn't match.
# concentration of Cl is used to determine the correct value.
df['EC value [microS/cm]']['F 4.1'] = df['EC [µS/cm]']['F 4.1']
df['EC [µS/cm]']['F 9.1'] = df['EC value [microS/cm]']['F 9.1']
df['EC [µS/cm]']['F 2.1'] = df['EC value [microS/cm]']['F 2.1']

#%% write combined and altered dataset

# set output path
outpath = os.path.join(repo_dir, r'Data\WorkingData\prepared_dataset_v1.csv')
# write output (input DataAnalysis.py)
df.to_csv(outpath)

