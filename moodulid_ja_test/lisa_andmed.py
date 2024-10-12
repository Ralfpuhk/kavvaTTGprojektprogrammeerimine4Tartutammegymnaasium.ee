from spire.xls import *
from spire.xls.common import *

import os
import pandas as pd #pip install openpyxl
import numpy as np

import time
import datetime
import discordwebhook
from discordwebhook import Discord


def lisa(row, input_kuupaev, input_kell, input_sonum, user):
    
    assignment = [input_kuupaev, input_kell, input_sonum]
    column = ["A", "B", "C"]
    for num in column:
        cell = ("%s%s" % (num, row))
        sheet.Range[cell].Text = assignment[column.index(num)]
        
    path = ("info/"+ user_ID +".xlsx")
    # Save to a .xlsx file
    wb.SaveToFile(path, FileFormat.Version2016)
    return

dir_path = "info/"
file_list = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
            
        file_list.append(os.path.basename(path).split('/')[-1])

# Create a Workbook object
wb = Workbook()
# Remove default worksheets
wb.Worksheets.Clear()
# Add a worksheet and name it "Employee"
sheet = wb.Worksheets.Add("kalender")



user_ID = input("Input your custom ID: ")
if (user_ID) + ".xlsx" not in file_list:
    i=1
    lisa(i,".",".",".", user_ID)


    

while True:
    sonum = input("Input message: ")
    kuupaev = input("Input date (d/dd.m/mm.yyyy): ")#kontrolli hiljem kuida need vormistatud
    kell = input("Input time(x/xx:y/yy): ")

    if (user_ID) + ".xlsx" in file_list:
        df = pd.read_excel(os.path.join(dir_path, user_ID) + ".xlsx", header=None)  # Read without headers to get raw data
        
        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
        for info in matrix:
            if info[1] == ".":
                i = matrix.index(info) + 1
                lisa(i, kuupaev, kell, sonum, user_ID)
                lisa((i+1),".",".",".", user_ID)


#i = lisa(i, kuupaev2, kell2, sonum2, user_ID)



