import os
import glob
import pandas as pd
import numpy as np
import xlrd

path = 'C:/Users/al146/Desktop/New folder3/'

# creats a list of all files with .csv format in above path.
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

# a function for merging csv files and saving the clean result
def mergeCSV(fileslist):
    result = pd.DataFrame()
    for file in fileslist:
        table = pd.read_csv(file)
        result = result.append(table, ignore_index=True)
    result.to_csv('resultweather.csv')

mergeCSV(files)