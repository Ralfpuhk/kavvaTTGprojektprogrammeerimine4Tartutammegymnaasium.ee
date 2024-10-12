from spire.xls import *
from spire.xls.common import *
from spire.xls import Workbook

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
wb = Workbook()

directory_name = "info"

# Create the directory
try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
            
        file_list.append(os.path.basename(path).split('/')[-1])

user_ID = input("Input your custom ID: ")
if (user_ID) + ".xlsx" not in file_list:
    # Remove default worksheets
    wb.Worksheets.Clear()
    # Add a worksheet and name it "Employee"
    sheet = wb.Worksheets.Add()
    i=1
    lisa(i,".",".",".", user_ID)


    

while True:
    sonum = input("Input message: ")
    kuupaev = input("Input date (d/dd.m/mm.yyyy): ")#kontrolli hiljem kuida need vormistatud
    kell = input("Input time(x/xx:y/yy): ")

    if (user_ID) + ".xlsx" in file_list:
        df = pd.read_excel(os.path.join(dir_path, user_ID) + ".xlsx", header=None)  # Read without headers to get raw data
        
        wb = Workbook()
        wb.LoadFromFile("info/"+ user_ID +".xlsx")
        sheet = wb.Worksheets["kalender"]
        
        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
        for info in matrix:
            if info[1] == ".":
                i = matrix.index(info) + 1
                lisa(i, kuupaev, kell, sonum, user_ID)
                lisa((i+1),".",".",".", user_ID)
                print(matrix)


#i = lisa(i, kuupaev2, kell2, sonum2, user_ID)



