# -*- coding: utf-8 -*-
"""
Title: "DataVisualisation"
Author: "Frank van Broekhoven"
ORCiD: https://orcid.org/0009-0008-1593-9842
Date: '2024-06-24'
General info:
    
    This script is part of the article
    - vanBroekhoven et al.(2024) Linking recharge water sources to groundwater composition in the Hindon subbasin of the Ganges River, India.
    
    This script is used for:
    - to make the raw figures used in the article
        - figure 2 (PDF)
        - figure 3 (PDF)
        - figure 4 (PDF)
        - figure 5 (PDF)
        - calculates tables 1 and S1
        - supplementary figures S1 and S6

"""
#%% Import modules
import pandas as pd
import geopandas as gpd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import os

# Set pdf.fonttype to make sure that the figure labels are 'text' in the pdf exports and not 'outlines'
matplotlib.rcParams['pdf.fonttype'] = 42 

#%% Read dataset

# set path
repo_dir = r'C:\GitHub\Temp_CleaningTheGanga_Paper1' # change this to the location where you stored the reposiotry
path = os.path.join(repo_dir, r'Data\WorkingData\analysed_dataset_v1.csv')

# read dataset (output DataAnalysis.py)
df = pd.read_csv(path, index_col=('Sample ID'))

#%% Function to make scatter plots

def scatter_plot_Frank(x, y, variable=None, style='Type', xy_line=False, trend=False, manual_colours=False):
    """
    Creates a scatter plot with optional labels, trendline, and x=y line.
    
    Parameters:
    - x (str): The column name for the x-axis values in the dataframe.
    - y (str): The column name for the y-axis values in the dataframe.
    - variable (str, optional): The column name to use for color coding the points. Default is None.
    - style (str): The column name to use for styling the points. Default is 'Type'.
    - xy_line (bool): If True, adds a y=x line to the plot. Default is False.
    - trend (bool): If True, adds a trendline to the plot. Default is False.
    - manual_colours (bool): If True, uses a predefined color palette. Default is False.
    
    Returns:
    - fig: The created figure.
    - ax: The axes of the created figure.
    """
    # Create a new figure and axis
    fig, ax = plt.subplots()
    
    # Set the hue for the scatter plot
    if variable:
        hue = df[variable]
    else:
        hue = None

    # Plot the scatter plot with or without manual colours   
    if manual_colours:
        palette={'1':"darkorange", '2':"dodgerblue", '3':"gold",'4':"limegreen",'village pond':"red",'irrigation canal':"slateblue"}
        sns.scatterplot(ax=ax, x=df[x], y=df[y], hue=hue, style=df[style], palette=palette, s=200, zorder=2)
    else:
        sns.scatterplot(ax=ax, x=df[x], y=df[y], hue=hue, style=df[style], palette="Spectral_r", s=200, zorder=2)

    # Add label to each point    
    for i, label in enumerate(df.index):
        plt.annotate(label, (df[x][i], df[y][i]))
    
    # Set axis labels and grid
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    
    # Optionally add a y=x line  
    if xy_line:
        lims = [np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
                np.max([ax.get_xlim(), ax.get_ylim()])]  # max of both axes
        ax.plot(lims, lims, alpha=0.75, zorder=0, linestyle='--', color='grey')
        ax.set_aspect('equal')
        ax.set_xlim(lims)
        ax.set_ylim(lims)
        
    # Optionally add a trendline    
    if trend:
        # Calculate the trendline
        a,b = np.polyfit(df[x], df[y], 1)  #y = ax+b
        poly = np.poly1d([a,b])
        
        # plot trendline
        xx = np.linspace(df[x].min(), df[x].max(), 500)
        plt.plot(xx, poly(xx))
        
        # Display the trendline formula on the plot
        text = f'y = {a:0.2f}x + {b:0.2f}'
        plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    
    # Show the plot
    plt.show()
    
    return fig, ax

#%% Scatter plots: figure 3 and figure 5

### Figure 3: Scatter plot of stable isotopes

# Define the variables and plot the scatter plot
x = 'dO18'
y = 'dD'
fig, ax = scatter_plot_Frank(x, y, style='cluster', variable='cluster', trend=True, manual_colours=True)

#add Local Meteoric Water Line (LMWL) to isotope scatter plot
def LMWL(d18O):
    """
    Calculate d2H based on d18O
    
    Parameters:
    - d18O: Oxygen-18 isotope ratio.
    
    Returns:
    - d2H: Deuterium isotope ratio.
    """
    d2H = 7.15 * d18O + 2.60    #Delhi [Pang et al., 2004 in Joshi et al., 2018]
    #d2H = 7.9 * d18O + 5.56    #study area of Joshi et al., 2018
    #d2H = 8.14 * d18O + 10.9   #global
    return d2H

# Get the current x-axis limits from the plot
x_min, x_max = plt.gca().get_xlim()

# Plot the LMWL line on the scatter plot
plt.plot([x_min, x_max], [LMWL(x_min), LMWL(x_max)], color='grey', linestyle='--', label='LMWL Delhi')
plt.legend()

# Export Figure 3 as a PDF file
outpath_fig3 = os.path.join(repo_dir, 'Output/Figure_3.pdf')
plt.savefig(outpath_fig3, format='pdf', bbox_inches="tight")


### Figure 5: Scatter plot of d18O and distance to the nearest irrigation canal

# Define the variables and plot the scatter plot
x = 'distance to canal [m]'
y = 'dO18'
fig, ax = scatter_plot_Frank(x, y, style='cluster', variable='cluster', manual_colours=True)

# Export Figure 5 as a PDF file
outpath_fig5 = os.path.join(repo_dir, 'Output/Figure_5.pdf')
plt.savefig(outpath_fig5, format='pdf', bbox_inches="tight")

#%% Function to plot cross-sections

# Load elevation profile
profile_path = os.path.join(repo_dir, r'Data/StartData/DataForFigures/elevation_profile_v1.csv')
df_profile = pd.read_csv(profile_path)

# Load Points of Interest (POIs) along the cross-section
POI_path = os.path.join(repo_dir, r'Data/StartData/DataForFigures/POIs_along_transect_v2.geojson')
gdf_POI = gpd.read_file(POI_path)

# Set default elevation for all POIs
gdf_POI['y'] = 250

# Adjust elevation for specific types of POIs to make sure they don't overlap
gdf_POI.loc[gdf_POI['type']=='River', 'y']              = 250
gdf_POI.loc[gdf_POI['type']=='Industry', 'y']           = 260
gdf_POI.loc[gdf_POI['type']=='Irrigation canal', 'y']   = 250
gdf_POI.loc[gdf_POI['type']=='Village', 'y']            = 255

# Define paths to images for different types of POIs
type_images = {
    'Industry'          : plt.imread(os.path.join(repo_dir, 'Data\StartData\DataForFigures\POI_symbols\Industry.png')),  # Provide the path to your image file
    'Village'           : plt.imread(os.path.join(repo_dir, 'Data\StartData\DataForFigures\POI_symbols\house.png')),
    'Irrigation canal'  : plt.imread(os.path.join(repo_dir, 'Data\StartData\DataForFigures\POI_symbols\canal.png')),
    'River'             : plt.imread(os.path.join(repo_dir, 'Data\StartData\DataForFigures\POI_symbols\River.png')),
    }

# Define zoom levels for POI images
zoom_images = {
    'Industry'          : 0.025,
    'Village'           : 0.025,
    'Irrigation canal'  : 0.2,
    'River'             : 0.1,
    }

# Package POI data into a list
POI = [gdf_POI, type_images, zoom_images]


def crosssection_plot(df, parameter, style='cluster', label='Sample ID', profile=df_profile, POI=POI, palette='Spectral_r'):
    """
    Plots a cross-section figure with sample data, elevation profile, and POIs.

    Parameters:
    - df: DataFrame containing sample data with 'distance startpoint Yamuna [m]' and 'depth [mMSL]' columns.
    - parameter: Column name in df to use for coloring the scatter plot points.
    - style: Column name in df to use for styling the scatter plot points. Default is 'cluster'.
    - label: Column name in df to use for labeling points. Default is 'Sample ID'.
    - profile: DataFrame containing the elevation profile with 'Distance_startpoint_Yamuna' and 'depth_MSL' columns.
    - POI: List containing POI data [gdf_POI, type_images, zoom_images].
    - palette: Color palette to use for the scatter plot. Default is 'Spectral_r'.

    Returns:
    - fig: The created figure.
    - ax: The axes of the created figure.
    """
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=[30,10])
    
    # Plot sample data with scatter plot
    sns.scatterplot(ax=ax, x=df['distance startpoint Yamuna [m]'], y=df['depth [mMSL]'], hue=df[parameter], style=df[style], palette=palette, s=200, zorder=2)
    
    # Add labels to the points if label parameter is provided
    if label:
        df['Sample ID'] = df.index
        def plotlabel(xvar, yvar, label):
            ax.text(xvar+200, yvar, label, rotation=0)  # Rotate the label by 45 degrees)
        df.apply(lambda x: plotlabel(x['distance startpoint Yamuna [m]'],  x['depth [mMSL]'], x[label]), axis=1)
    
    # Plot the elevation profile line
    ax.scatter(df_profile['Distance_startpoint_Yamuna'], df_profile['depth_MSL'], c='black', s=1, zorder=1)
    ax.plot(df_profile['Distance_startpoint_Yamuna'], df_profile['depth_MSL'], color='black',  zorder=0)
    
    # Add POIs to the plot
    if POI: 
        gdf_POI = POI[0]
        type_images = POI[1]
        zoom_images = POI[2]
        for index, point in gdf_POI.iterrows():
            ab = matplotlib.offsetbox.AnnotationBbox(
                    matplotlib.offsetbox.OffsetImage(type_images[point['type']], zoom=zoom_images[point['type']]),
                    (point['HubDist'], point['y']), 
                    frameon=False
                    )
            plt.gca().add_artist(ab)
    
    # Set axis labels and limits
    ax.set_xlabel('Distance along transect [m]')
    ax.set_ylabel('Depth [mMSL]')
    ax.set_xlim(23000, 72000) 
    ax.set_ylim(140, 270) 
    fig.tight_layout()
    plt.show()
    
    return fig, ax

#%% Cross-section plots: figure 2 and figure 4

### Figure 2: Cross-section plot for clusters

# Define the palette for clusters
palette={'1':"darkorange", '2':"dodgerblue", '3':"gold",'4':"limegreen",'village pond':"red",'irrigation canal':"slateblue"}

# Cross-section plot for clusters
crosssection_plot(df=df, parameter='cluster', label='Sample ID', palette=palette) 

# Export Figure 2 as a PDF file
outpath_fig2 = os.path.join(repo_dir, 'Output/Figure_2.pdf')
plt.savefig(outpath_fig2, format='pdf', bbox_inches="tight")


### Figure 4: Cross-section plot for isotopes ('dO18')
crosssection_plot(df=df, parameter='dO18', label='Sample ID') 

# Export Figure 4 as a PDF file
outpath_fig4 = os.path.join(repo_dir, 'Output/Figure_4.pdf')
plt.savefig(outpath_fig4, format='pdf', bbox_inches="tight")


### Figures S6: crossection for each variable

# List of all variables to plot a cross-section
variables_to_plot = ['EC value [microS/cm]', 'pH', 'Hard [mg/L]', 'Alk [mg/L]', 
                      'Cl [mg/L]', 'NO3 [mg/L]', 'SO4 [mg/L]', 'F [mg/L]', 'NO2 [mg/L]', 'Na [mg/L]', 
                      'K [mg/L]', 'Ca [mg/L]', 'Mg [mg/L]', 'NH4 [mg/L]', 'Silica [mg/L]', 'COD [mg/L]', 
                      'B  [µg/L]', 'Al [µg/L]', 'V [µg/L]', 'Cr [µg/L]', 'Mn [µg/L]', 'Fe [µg/L]',
                      'Co [µg/L]', 'Ni [µg/L]', 'Cu [µg/L]', 'Zn [µg/L]', 'As [µg/L]', 'Se [µg/L]', 
                      'Sr [µg/L]', 'Cd [µg/L]', 'Ba [µg/L]', 'Pb [µg/L]', 'U [µg/L]', 'dO18', 'dD']

# loop to plot each and export (jpg) each variable
for variable in variables_to_plot:
    fig, ax = crosssection_plot(df=df, parameter=variable)
    #set path and export figure
    outpath_S6 = os.path.join(repo_dir, f'Output/Supplementary Material/Figure_S6_{variable.split()[0]}.jpg')
    fig.savefig(outpath_S6, bbox_inches="tight")
    

#%% Table 1: tabel with means per cluster 

# Define columns to analyze for each cluster
columns_to_analyse = ['EC value [microS/cm]', 'pH', 'Hard [mg/L]', 'Alk [mg/L]', 
                      'Cl [mg/L]', 'NO3 [mg/L]', 'SO4 [mg/L]', 'F [mg/L]', 'NO2 [mg/L]', 'Na [mg/L]', 
                      'K [mg/L]', 'Ca [mg/L]', 'Mg [mg/L]', 'NH4 [mg/L]', 'Silica [mg/L]', 'COD [mg/L]', 
                      'B  [µg/L]', 'Al [µg/L]', 'V [µg/L]', 'Cr [µg/L]', 'Mn [µg/L]', 'Fe [µg/L]',
                      'Co [µg/L]', 'Ni [µg/L]', 'Cu [µg/L]', 'Zn [µg/L]', 'As [µg/L]', 'Se [µg/L]', 
                      'Sr [µg/L]', 'Cd [µg/L]', 'Ba [µg/L]', 'Pb [µg/L]', 'U [µg/L]']

# Calculate mean values for each cluster group
output = df.groupby(['cluster'], as_index=False).agg(['mean'])

# Select only the specified columns for analysis
output = output[columns_to_analyse]

# Transpose the dataframe to switch rows and columns for better readability
transposed = output.transpose()
transposed.index = transposed.index.droplevel(1)

# Calculate mean and Standard deviation values for all groundwater samples together
# select groundwater samples and variables to analyse
selection = df.loc[df['Type'].isin(['deep tubewell', 'shallow tubewell'])]
selection = selection[columns_to_analyse]

# Calculate mean values for all groundwater samples
total_mean = selection.mean()
# # Calculate standard deviation for all groundwater samples
total_std = selection.std()

# Standardize group means relative to the mean of all groundwate samples
cluster_standarized = pd.DataFrame()
for column in transposed.columns:
    cluster_standarized[column] = (transposed[column] - total_mean) / total_std
standardized_T = cluster_standarized

# Create a heatmap with a colorbar centered around zeros
fig, ax = plt.subplots(figsize=[10,15])
maximum = 2 # Set maximum value for color scale
sns.heatmap(standardized_T, cmap = 'coolwarm', ax=ax, annot=transposed, fmt='.2f', yticklabels = 1 , vmin=-maximum, vmax=maximum)
plt.xticks(rotation = 45)
fig.set_tight_layout(True)

# Export table 1 as a jpg file
outpath_tab1 = os.path.join(repo_dir, 'Output/Table_1.jpg')
plt.savefig(outpath_tab1, bbox_inches="tight")


#%% Table S2: univariate overview of groundwater samples

# Define columns to analyze for univariate overview
columns_to_analyse = ['EC value [microS/cm]', 'pH', 'Hard [mg/L]', 'Alk [mg/L]', 
                      'Cl [mg/L]', 'NO3 [mg/L]', 'SO4 [mg/L]', 'F [mg/L]', 'NO2 [mg/L]', 'Na [mg/L]', 
                      'K [mg/L]', 'Ca [mg/L]', 'Mg [mg/L]', 'NH4 [mg/L]', 'Silica [mg/L]', 'COD [mg/L]', 
                      'B  [µg/L]', 'Al [µg/L]', 'V [µg/L]', 'Cr [µg/L]', 'Mn [µg/L]', 'Fe [µg/L]',
                      'Co [µg/L]', 'Ni [µg/L]', 'Cu [µg/L]', 'Zn [µg/L]', 'As [µg/L]', 'Se [µg/L]', 
                      'Sr [µg/L]', 'Cd [µg/L]', 'Ba [µg/L]', 'Pb [µg/L]', 'U [µg/L]', 'dO18', 'dD']

#select only groundwater samples and columns to analyse
gws = df.loc[df['Type'].isin(['deep tubewell', 'shallow tubewell'])]
gws = gws[columns_to_analyse]

# Get description and transpose the dataframe to switch rows and columns for better readability
overview_gws = gws.describe().transpose()
print(overview_gws)

#%% FIGURE S1: correlation matrix

# Define columns to analyze for correlation matrix
columns_to_analyse = ['EC value [microS/cm]', 'pH', 'Hard [mg/L]', 'Alk [mg/L]', 
                      'Cl [mg/L]', 'NO3 [mg/L]', 'SO4 [mg/L]', 'F [mg/L]', 'NO2 [mg/L]', 'Na [mg/L]', 
                      'K [mg/L]', 'Ca [mg/L]', 'Mg [mg/L]', 'NH4 [mg/L]', 'Silica [mg/L]', 'COD [mg/L]', 
                      'B  [µg/L]', 'Al [µg/L]', 'V [µg/L]', 'Cr [µg/L]', 'Mn [µg/L]', 'Fe [µg/L]',
                      'Co [µg/L]', 'Ni [µg/L]', 'Cu [µg/L]', 'Zn [µg/L]', 'As [µg/L]', 'Se [µg/L]', 
                      'Sr [µg/L]', 'Cd [µg/L]', 'Ba [µg/L]', 'Pb [µg/L]', 'U [µg/L]', 'dO18', 'dD',
                      'depth [m]'
                      ]

# Select only groundwater samples and columns to analyse
df = df.loc[df['Type'].isin(['deep tubewell', 'shallow tubewell'])]
df_selection = df[columns_to_analyse]

# Plot correlation matrix
g = sns.clustermap(df_selection.corr(), 
                    method = 'complete', 
                    cmap   = 'RdBu', vmin=-1, vmax=1,
                    annot  = True, 
                    annot_kws = {'size': 8},
                    yticklabels = 1 , xticklabels = 1,
                    figsize=[20,15])
plt.setp(g.ax_heatmap.get_xticklabels(), rotation=60)

# Export figure S1 as a jpg file
outpath_S1 = os.path.join(repo_dir, 'Output/Supplementary Material/Figure_S1.jpg')
plt.savefig(outpath_S1, bbox_inches="tight")