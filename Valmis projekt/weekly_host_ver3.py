import tkinter as tk

from tkcalendar import Calendar
import customtkinter as ctk
import time
import datetime
import tkinter.scrolledtext as scrolledtext

from spire.xls import *
from spire.xls.common import *
from spire.xls import Workbook

import os
import pandas as pd #pip install openpyxl
import numpy as np

import discordwebhook
from discordwebhook import Discord

import socket

import re
import httplib2
import requests 
from bs4 import BeautifulSoup

# ////////////////////////////////
def on_closing():
    root.destroy()
    
def digdin(message, nimi):
    discordWebhook = "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
    discord = Discord(url=discordWebhook)#

    discord.post(content = ("The venerable <@"+(str(nimi[:len(nimi)-5]))+">" + " hath conjured forth a decree that the following notification shall sound through the halls: \n" + str(message)))


def file_list_cck():
    file_list = []
    
    for path in os.listdir(dir_name_slash):
        if os.path.isfile(os.path.join(dir_name_slash, path)):           
            file_list.append(os.path.basename(path).split('/')[-1])
    return(file_list)

def check():
    
    current_time = datetime.datetime.now()		#current everything (year-month-day-hour-minute)
    month = datetime.date.today().month		# current month
    day = datetime.date.today().day		# current day
    hour = datetime.datetime.now().hour   # current hour
    minute = datetime.datetime.now().minute #  current minute
    year = datetime.datetime.now().year
    second = datetime.datetime.now().second
    
    
    for file in file_list_cck():
        
        df = pd.read_excel(os.path.join(dir_name_slash, file), header=None)  # Read without headers to get raw data

        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
#         print(matrix[1:])
#         print(matrix[-1][1])
        for info in matrix:  
            
            if info[0] == ((str(day) + "." + str(month) + "." + str(year))):
                print(info[0])
                if info[1] == (str(hour) + ":" + str(minute)):
#                     print(info[1])
                    #if lll == 1:
                    digdin(info[2], file)
#                     print(info[2])
        if matrix[-1][1] == (str(hour) + ":" + str(minute)):
            
            url = 'https://www.postimees.ee/'
            response = requests.get(url) 
      
            soup = BeautifulSoup(response.text, 'html.parser') 
            headlines = soup.find('body').find_all('h2')

            uudis = []
            lingid = []
            
            for link in soup.find_all("a", href = re.compile("^https://arvamus.postimees.ee"))[9:12]:
                lingid.append(link.get("href"))
            discordWebhook = "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
            discord = Discord(url=discordWebhook)#
            
            discord.post(content = "Hearken, good folk, to the tidings from Postimees on the date of " + str(day) + "." + str(month) + "." + str(year) + "\n\n" + (lingid[0]+" "+lingid[1]+" "+lingid[2]))
        
    second = datetime.datetime.now().second                    #lll =+ 1
    print("cycle done. Current second count is : " + str(second))
    root.after(60000, check)

def recieve_xslx(conn):

    # Receive the length of the file name first (4 bytes)
    byte_length = conn.recv(4)
    byte_length_update = int.from_bytes(byte_length, 'big')  # Convert bytes to integer

    flyname_bytes = conn.recv(byte_length_update)  # Read the specified length of bytes for the file name
    flyname = flyname_bytes.decode('utf-8')  # Decode the filename
    flypath = os.path.join(dir_name, flyname)  # Create the full file path in the 'info' dir_name
    print(flypath)
    # Open a file to write the received data
    with open(flypath, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("recieved")


def send_xslx(send11, conn):
    flyfile = os.path.join(dir_name, send11)  # Full path to the file
    print(f"Sending file: {flyfile}")
    
    # Open the file in binary read mode
    with open(flyfile, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:  # Check if there's no more data to read
                break
            conn.sendall(data)  # Send the chunk of data
#             print(f"Sent {len(data)} bytes")
    
    print(conn.recv(1024).decode("utf-8"))       
    conn.sendall(b"EOF")  # Send an empty byte to signal the end of transmission
    print("File sent successfully.")

def connection():
    s = socket.socket()
    s.close
    s.bind((IP, port))
    s.settimeout(3)
    try:
        s.listen(1)
        print("trying for connection...")
        conn, addr = s.accept()
        print("connected! :", addr)
        
        data = conn.recv(1024)
        print(data)
        flyfile_name = data.decode() + ".xlsx"
        print(flyfile_name)
        print(file_list_cck())
        
        
        if flyfile_name in file_list_cck():
            print("flyfile found")
            conn.sendall("1".encode("utf-8"))
            send_xslx(flyfile_name, conn)
            
            recieve_xslx(conn) 
            
        elif flyfile_name not in file_list_cck():
            print("flyfile not found")
            conn.sendall("0".encode("utf-8"))
            
            recieve_xslx(conn)            
                
        else:
            print("oopsy :), bokem")
        conn.close()       
    except:
        print("no connection found")
    
    print("closing conn")
    s.close()
    root.after(1000, connection)
    

# ////////////////////////////////

dir_name_slash = "info/"
dir_name = "info"
port = 54123
IP = "192.168.1.142" # hosti IP
# IP = "127.0.0.1"

# ///////////////////////////////

try:
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{dir_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{dir_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
    
root = ctk.CTk()

# ///////////////////////////////

root.after(0, check)
root.after(0, connection)

# ///////////////////////////////

root.mainloop()
