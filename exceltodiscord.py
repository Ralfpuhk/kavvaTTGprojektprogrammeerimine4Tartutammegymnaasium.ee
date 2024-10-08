import os
import pandas as pd #pip install openpyxl
import numpy as np

import time
import datetime
import discordwebhook
from discordwebhook import Discord      #!importante! mdea kas ise kirjutatud .xlsx    

def digdin(message, nimi):
    discordWebhook = "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
    discord = Discord(url=discordWebhook)#

    discord.post(content = (str(nimi[:len(nimi)-5]) + " has set the following notification to go off now: \n\n" + str(message)))

dir_path = "info/"

file_list = []
file_amount = 0

while True:
    
    
    
    
    
    
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            
            file_amount += 1
            file_list.append(os.path.basename(path).split('/')[-1])
            
#print('File count:', file_amount)
#print(file_list)
        

    for file in file_list:
        df = pd.read_excel(os.path.join(dir_path, file), header=None)  # Read without headers to get raw data
        
        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
        #print(matrix)
        for info in matrix:
            
            #lll = 1
        
            current_time = datetime.datetime.now()		#current everything (year-month-day-hour-minute)
            month = datetime.date.today().month		# current month
            day = datetime.date.today().day		# current day
            hour = datetime.datetime.now().hour   # current hour
            minute = datetime.datetime.now().minute #  current minute
            year = datetime.datetime.now().year
        

            if info[0] == ((str(day) + "." + str(month) + "." + str(year))):
                if info[1] == (str(hour) + ":" + str(minute)):
                    #if lll == 1:
                    digdin(info[2], file)
                    print(info[2])
                        #lll =+ 1
    time.sleep(60)
    print("cycle done")
    #print("xxxxxxxxxxxxxxxxxxxxxxx")
    #print(" ")
    #print(file)
    #print(" ")
    #print(matrix)

#print('File count:', file_amount)
