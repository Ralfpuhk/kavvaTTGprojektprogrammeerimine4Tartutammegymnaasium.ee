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

# ////////////////////////////////
def on_closing():
    root.destroy()
    
def digdin(message, nimi):
    discordWebhook = "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
    discord = Discord(url=discordWebhook)#

    discord.post(content = ("<@"+(str(nimi[:len(nimi)-5]))+">" + " has set the following notification to go off now: \n" + str(message)))


def file_list_cck():
    file_list = []
    
    for path in os.listdir(dir_name_slash):
        if os.path.isfile(os.path.join(dir_name_slash, path)):           
            file_list.append(os.path.basename(path).split('/')[-1])
    return(file_list)

def check():
    

    for file in file_list_cck():
        df = pd.read_excel(os.path.join(dir_name_slash, file), header=None)  # Read without headers to get raw data
        
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
            second = datetime.datetime.now().second  

            if info[0] == ((str(day) + "." + str(month) + "." + str(year))):
                if info[1] == (str(hour) + ":" + str(minute)):
                    #if lll == 1:
                    digdin(info[2], file)
                    print(info[2])
    second = datetime.datetime.now().second                    #lll =+ 1
    print("cycle done. Current second count is : " + str(second))
    root.after(60000, check)

def recieve_xslx(conn):


    byte_length = conn.recv(4) #votab vastu faili nime pikkuse byteides
    byte_length_update = int.from_bytes(byte_length, 'big')  # muudab numbriks

    flyname_bytes = conn.recv(byte_length_update)  # votab vastu faili ja kasutab selle pikkust selleks?
    flyname = flyname_bytes.decode('utf-8')
    flypath = os.path.join(dir_name, flyname)
    print(flypath)

    with open(flypath, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("recieved")


def send_xslx(send11, conn):
    flyfile = os.path.join(dir_name, send11) 
    print(f"Sending file: {flyfile}")

    with open(flyfile, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            conn.sendall(data) # mdea, miks see ei saada tyhja hulka?????
            print(f"Sent {len(data)} bytes")
    
    print(conn.recv(1024).decode("utf-8"))       
    conn.sendall(b"EOF")  # ma olen 6h debuginud seda. annan alla. lic brute force method
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
IP = "127.0.0.1" # hosti IP

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
