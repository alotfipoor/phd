import os
import glob
import pandas as pd
import numpy as np
import xlrd

path = 'C:/Users/al146/OneDrive - Heriot-Watt University/Data/Findhorn/Raw/'

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
        table = pd.DataFrame(columns=['file_id'])
        table.loc[len(table)] = file
        filecsv = open(file)
        table['total_no'] = len(filecsv.readlines())
        df = pd.read_csv(file, names=['time', 'meter'])
        table['zero_no'] = sum((df == 0).sum(axis=1))
        table['na_no'] = sum(pd.isnull(df['meter']))
        table['zero%'] = (table['zero_no']/table['total_no'])*100
        table['na%'] = (table['na_no']/table['total_no'])*100
        result = result.append(table, ignore_index=True)
    result.file_id.replace({'C:/Users/al146/OneDrive - Heriot-Watt University/Data/Findhorn/Raw/':''}, regex=True, inplace=True)
    result.to_csv('result.csv')

mergeCSV(files)