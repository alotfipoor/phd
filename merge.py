import os
import glob
import pandas as pd
import numpy as np
import xlrd

path = 'C:/Users/al146/Desktop/New folder/'

# creats a list of all files with .csv format in above path.
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

# a functon for replacing the date format of excel with python
def read_date(date):
    return xlrd.xldate.xldate_as_datetime(date, 0)

# a function for merging csv files and saving the clean result
def mergeCSV(fileslist):
    result = pd.DataFrame()
    for file in fileslist:
        table = pd.read_csv(file, names=['time', 'meter_reading'])
        table['timestamp'] = pd.to_datetime(table['time'].apply(read_date), errors='coerce')
        table_time = table.drop(['time'], axis=1)
        table_time['site_id'] = file
        result = result.append(table_time, ignore_index=True)
    result.site_id.replace({'_\(2015-02-15,42days\).csv':''}, regex=True, inplace=True)
    result.site_id.replace({'C:/Users/al146/Desktop/New folder/Processed-':''}, regex=True, inplace=True)
    result.site_id.replace({'D_1Ph_':''}, regex=True, inplace=True)
    result.site_id.replace({'_mf':''}, regex=True, inplace=True)
    result.to_csv('result.csv')
    result.to_pickle('clean_data')

mergeCSV(files)