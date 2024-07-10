# -*- coding: utf-8 -*-
"""
Title: "DataAnalysis"
Author: "Frank van Broekhoven"
ORCiD: https://orcid.org/0009-0008-1593-9842
Date: '2024-06-24'
General info:
    
    This script is part of the article
    - vanBroekhoven et al.(2024) Linking recharge water sources to groundwater composition in the Hindon subbasin of the Ganges River, India.
    
    This script is used for:
    - log transform and standardize the variables
    - Factor analysis with varimax rotation
    - Agglomerative Hierarchical Clustering analysis
    - Check electro-neutrality
    - plots supplementary figures S3 and S4

"""
#%% import modules
import pandas as pd
import numpy as np
import os
from factor_analyzer.factor_analyzer import FactorAnalyzer
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
import seaborn as sns

#%% read combined and altered dataset

# set path
repo_dir = r'C:\GitHub\Temp_CleaningTheGanga_Paper1' # change this to the location where you stored the reposiotry
path = os.path.join(repo_dir, r'Data\WorkingData\prepared_dataset_v1.csv')
# read dataset (output DataPreparations.py)
df = pd.read_csv(path, index_col=('Sample ID'))


#%% Factor Analysis and Cluster Analysis

### step 1: select only groundwater samples and columns to analyse

# select groundwater samples
df_GW = df.loc[df['Type'].isin(['deep tubewell', 'shallow tubewell'])]

#take field EC values, and lab pH values, drop TDS
columns_to_analyse = ['EC value [microS/cm]', 'pH', 'Hard [mg/L]', 'Alk [mg/L]', 
                      'Cl [mg/L]', 'NO3 [mg/L]', 'SO4 [mg/L]', 'F [mg/L]', 'NO2 [mg/L]', 'Na [mg/L]', 
                      'K [mg/L]', 'Ca [mg/L]', 'Mg [mg/L]', 'NH4 [mg/L]', 'Silica [mg/L]', 'COD [mg/L]', 
                      'B  [µg/L]', 'Al [µg/L]', 'V [µg/L]', 'Cr [µg/L]', 'Mn [µg/L]', 'Fe [µg/L]',
                      'Co [µg/L]', 'Ni [µg/L]', 'Cu [µg/L]', 'Zn [µg/L]', 'As [µg/L]', 'Se [µg/L]', 
                      'Sr [µg/L]', 'Cd [µg/L]', 'Ba [µg/L]', 'Pb [µg/L]', 'U [µg/L]']
df_selection = df_GW[columns_to_analyse]


### step 2: logarithmically transformed and standardised

# Log transformation expect for pH, as pH is already logarithmic
df_log = pd.DataFrame()
for variable in columns_to_analyse:
    if variable in ('pH.1'):
        print(variable, ' pH is not log transformed, because it is already a log')
        df_log[variable] = df_selection[variable]
    else:
        print('log transform ', variable)
        df_log[f'{variable} log'] = np.log(df_selection[variable])

# Standardisation (Z-score): resulting in data with a mean of zero and a standard deviation of one
def standardize(X):
    '''
    Function to standardise the data, resulting in data with a mean of zero and a standard deviation of one
    '''
    # Mean
    X_mean = X.mean()
    # Standard deviation
    X_std = X.std()
    # Standardization
    Z = (X - X_mean) / X_std
    return Z
df_transformed = standardize(df_log)


### step 3: Factor analysis with varimax rotation

# set number of factors
n_factors = 3
# perform factor analysis with varimax rotation
fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='principal') # default method='minres'
fa.fit(df_transformed)

# loadings and factor variance (table S2)
loadings = pd.DataFrame(fa.loadings_,  columns=['F{}'.format(i+1) for i in range(n_factors)], index=df_transformed.columns)
print('Factor Loadings \n%s' %loadings)
factor_variance = pd.DataFrame(fa.get_factor_variance(), columns=['F{}'.format(i+1) for i in range(n_factors)], index=['sum squared loadings', 'proportional variance', 'cumulative variance'])
print(factor_variance)

# dataset with factors
df_reduced = pd.DataFrame(fa.transform(df_transformed), columns=['F{}'.format(i+1) for i in range(n_factors)], index=df_transformed.index)


### step 4: Agglomerative Hierarchical Clustering

#applied CA with FA to reduce variables
df_CA = df_reduced.copy()

# visualize clusters with dendrogram (figure S3)
dendrogram = True
if dendrogram:
    plt.figure(figsize=(10, 7))
    plt.title("Dendrogram")
    clusters = shc.linkage(df_CA, method='ward', metric="euclidean")
    shc.dendrogram(Z=clusters, labels=df_CA.index)
    plt.show()
    
    # Export figure S3 as a jpg file
    outpath_S3 = os.path.join(repo_dir, 'Output/Supplementary Material/Figure_S3.jpg')
    plt.savefig(outpath_S3, bbox_inches="tight")

# set number of clusters
n_clusters = 4
# perform clustering
clustering_model = AgglomerativeClustering(n_clusters, affinity='euclidean', linkage='ward')
clustering_model.fit(df_CA)
data_labels = clustering_model.labels_ + 1  # plus 1 because python starts with 0

# add cluster labels to the total dataframe
df_CA['cluster'] = data_labels
df['cluster'] = df_CA['cluster']
df['cluster'] = np.where(df['Type'].isin(['village pond', 'irrigation canal']), df['Type'], df['cluster'])
df['cluster'] = df['cluster'].apply(lambda x: str(int(x)) if isinstance(x, (int, float)) else x) # change cluster numbers to strings, '1' instead of '1.0'

#%% visualise factor values per cluster

# pairplot factors with clusters (figure S4)
sns.pairplot(df_CA, hue='cluster', palette='deep')

# Export figure S4 as a jpg file
outpath_S4 = os.path.join(repo_dir, 'Output/Supplementary Material/Figure_S4.jpg')
plt.savefig(outpath_S4, bbox_inches="tight")

#%% Check electro-neutrality

# dictionaries for cations and anions with parameter name and conversion factor from mg/L -> mEq/L  (valance/molar mass)
anions = {
    'Alk [mg/L]': 0.02,
    'SO4 [mg/L]': 0.02082,
    'Cl [mg/L]': 0.02821,
    'F [mg/L]': 0.05264,
    'NO2 [mg/L]': 0.02174,
    'NO3 [mg/L]': 0.01613,
    }

cations = {
    'Ca [mg/L]': 0.04990,
    'Mg [mg/L]': 0.08229,
    'Na [mg/L]': 0.04350,
    'K [mg/L]': 0.02558,
    'NH4 [mg/L]': 0.05544,
    }

# calculate sum of anions [mEq/L]
df['sum anions [mEq/L]'] = 0
for key in anions:
    df['sum anions [mEq/L]'] = df['sum anions [mEq/L]'] + (df[key] * anions[key])

# calculate sum of cations [mEq/L]
df['sum cations [mEq/L]'] = 0
for key in cations:
    df['sum cations [mEq/L]'] = df['sum cations [mEq/L]'] + (df[key] * cations[key])

# calculate Anion-Cation Balance Differece
df['an/cat_diff%'] = (df['sum cations [mEq/L]'] - df['sum anions [mEq/L]']) / (df['sum cations [mEq/L]'] + df['sum anions [mEq/L]']) *100


#%% Export total dataset

#set path
outpath = os.path.join(repo_dir, r'Data\WorkingData\analysed_dataset_v1.csv')
# write dataset (input DataVisualisation.py)
df.to_csv(outpath)