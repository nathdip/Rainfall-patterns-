#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:05:50 2017

@author: atlas
"""

import os, glob
import numpy as np
import pandas as pd
import seaborn as sns
import math

#importing the data
current_directory = os.getcwd()
dir_list = next(os.walk('.'))[1]

os.chdir(dir_list[0])
files_xls  = glob.glob('*.xls')
data_pcp = pd.read_excel(files_xls[0])
pcp_filenames = data_pcp.iloc[:,1]
pcp_location = data_pcp.iloc[:, 2:4]
pcp_location = np.concatenate((pcp_location, np.zeros([len(pcp_location), 1])), axis = 1 )
pcp_dict = {}
for i in range(0, len(pcp_filenames)):
    
    data = open(pcp_filenames[i]+'.txt')

    try:
        precipitation = np.loadtxt(data, delimiter = ',', skiprows = 1)
        missing_data_counts = sum(precipitation == -999.0)
        print(missing_data_counts)
        if missing_data_counts == 0 :
            pcp_location[i][2] = 1
        else:
            pass
    except ValueError:
        pass

pcp_dataframe = pd. DataFrame(pcp_location, columns = ['Latitude','Longitude', 'Data Valid'])
pcp_dataframe.to_csv('stationverification_data_IMD_0.5deg_pcp.csv')

#latitude = pcp_location[:,0]
#longitude =  pcp_location[:, 1]
#stations = pcp_location[:, 2]
#import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
#import matplotlib.cm as cm
#fig = plt.figure(figsize=(8, 8))
#m = Basemap(projection='lcc', resolution='c',
#            width=4E6, height=4E6, 
#            lat_0=23.6, lon_0=76.8,)
#x1, y1 = m(longitude, latitude)
#m.drawmapboundary(fill_color='white') # fill to edge
#m.drawcountries()
#m.fillcontinents(color='white',lake_color='black',zorder=0)
#
#x1, y1 = m(longitude, latitude)
#m.scatter(x1,y1, c =stations, marker="o")
#plt.gray()
#plt.title("Flickr Geotagging Counts with Basemap")
#plt.show()
#m.pcolormesh(longitude, latitude,  stations, latlon = True, cmap = 'gray')
#m.scatter(x1, y1, s = stations, latlon = True, cmap = 'gray')
#plt.clim(0, 2)
#plt.colorbar(label = 'Stations')

#fig = plt.figure(figsize=(10, 8))
#m = Basemap(projection='lcc', resolution='c',
#            width=8E6, height=8E6, 
#            lat_0=23.6, lon_0=76.8,)
#m.shadedrelief(scale=0.5)
#m.pcolormesh(longitude, latitude, stations,
#             latlon=True, cmap='RdBu_r')
#plt.clim(-8, 8)
#m.drawcoastlines(color='lightgray')
#
#plt.title('January 2014 Temperature Anomaly')
#plt.colorbar(label='temperature anomaly (°C)');

# Map (long, lat) to (x, y) for plotting
#x, y = m(-122.3, 47.6)
#plt.plot(x, y, 'ok', markersize=5)
#plt.text(x, y, ' Seattle', fontsize=12);