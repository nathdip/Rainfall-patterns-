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

#importing the data
current_directory = os.getcwd()
dir_list = next(os.walk('.'))[1]

os.chdir(dir_list[3])
files_xls  = glob.glob('*.xls')
data_pcp = pd.read_excel(files_xls[0])
pcp_filenames = data_pcp['NAME']

pcp_dict = {}
for i in range(0, len(pcp_filenames)):
    data = open(pcp_filenames[i]+'.txt')
    precipitation = np.loadtxt(data, delimiter = ',')
    precipitation = precipitation[1:-1]
    missing_data_counts = sum(precipitation == -999.0)
    pcp_dict[pcp_filenames[i]] = missing_data_counts
    print(pcp_filenames[i], missing_data_counts)
print(pcp_dict)
    
