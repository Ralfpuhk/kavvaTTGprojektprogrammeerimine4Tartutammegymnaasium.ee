# TÖÖTAV PROTOTÜÜP
# Meelespea loomiseks pead vajutama kuupäeva peale ning sisestama kellaaja.
# Kellaaeg tuleb sisestada formaadis HH:MM nt 12:29 voi 01:32
# Kui kuupäev ja kellaaeg on valitud, vajuta "Loo meelespea", siis kirjuta selle kohale oma sonum ning vajuta "Salvesta".
# Salvestamine appendib Discord ID, kuupäeva, kellaaja ning meelespea ning kohandab andmed ja salvestab .xlsx faili.
# NB! Programm peab lahti olema, et see sonumi saadaks Discordi. (discordi server, millesse sonum saadetakse: https://discord.gg/qr4RssDH9J)
# Programm saadab teate minuti jooksul, kuna oleneb programmi avamise ajast -> ei pruugi olla iga minuti alguses.
# Kuidas saada oma discord ID: 
# Vajuta discordis all vasakul nupule "User Settings" -> Vajuta "Advanced" -> Käivita "Developer Mode" -> Mine seadetest välja -> All vasakul vajuta oma discordi profiili peale -> Vajuta "Copy User ID"
# Kasutajaliidese esteetikat peab veel arendama, aga programm teeb praegu oma töö ära.

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

def check():
    
    file_amount = 0
    file_list = []
       
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
            second = datetime.datetime.now().second  

            if info[0] == ((str(day) + "." + str(month) + "." + str(year))):
                if info[1] == (str(hour) + ":" + str(minute)):
                    #if lll == 1:
                    digdin(info[2], file)
                    print(info[2])
    second = datetime.datetime.now().second                    #lll =+ 1
    print("cycle done. Current second count is : " + str(second))
    root.after(60000, check)

def lisa(row, input_kuupaev, input_kell, input_sonum, user, sheet, wb):
    
    assignment = [input_kuupaev, input_kell, input_sonum]
    column = ["A", "B", "C"]
    for num in column:
        cell = ("%s%s" % (num, row))
        sheet.Range[cell].Text = assignment[column.index(num)]
        
    path = ("info/"+ user +".xlsx")
    # Save to a .xlsx file
    wb.SaveToFile(path, FileFormat.Version2016)
    return


def time_convert(date1):
    lista = []
    if "/" in date1:
        lista = date1.split("/")
        separator = "."
    elif ":" in date1:
        lista = date1.split(":")
        separator = ":"
        
    lias = []
    for pp in lista:
        date = pp.lstrip("0")
        lias.append(date)
    string = separator.join(lias)
    return(string)
    #print(string)

dir_path = "info/"
directory_name = "info"

def digdin(message, nimi):
    discordWebhook = "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
    discord = Discord(url=discordWebhook)#

    discord.post(content = ("<@"+(str(nimi[:len(nimi)-5]))+">" + " has set the following notification to go off now: \n" + str(message)))


try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Weekly")  
root.geometry("900x700")  


main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)


left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="y", padx=(0, 10))


discord_label = ctk.CTkLabel(left_frame, text="Discord ID:")
discord_label.pack(padx=10, pady=(10, 0))

discord_entry = ctk.CTkEntry(left_frame, width=100)
discord_entry.pack(padx=10, pady=(0, 10), expand=True)


mode_switch = ctk.CTkSwitch(left_frame, text="Light Mode", command=lambda: ctk.set_appearance_mode("Light" if ctk.get_appearance_mode() == "Dark" else "Dark"))
mode_switch.pack(pady=(10, 10))


right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)


today = datetime.date.today()
mindate = datetime.date(year=2000, month=1, day=1)
maxdate = today + datetime.timedelta(days=365)

cal = Calendar(right_frame,
                selectmode='day',
                locale='et',
                disabledforeground='red',
                cursor="hand2",
                background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],
                selectbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1],
                mindate=mindate,
                maxdate=maxdate,
                year=int(time.strftime('%Y')),
                month=int(time.strftime('%m')),
                day=int(time.strftime('%d')),
                width=30, height= 30)  
cal.pack(expand=True, fill="both", padx= 50)  


time_frame = ctk.CTkFrame(right_frame)
time_frame.pack(pady=(10, 0))  

time_label = ctk.CTkLabel(time_frame, text="Kell: ")
time_label.pack(side="left")

time_entry = ctk.CTkEntry(time_frame, width=50)  
time_entry.pack(side="left", padx=(0, 10))  


time_entry.delete(0, ctk.END)  


text_box = scrolledtext.ScrolledText(right_frame, width=70, height=10, wrap='word')  
text_box.pack(expand= True, fill="both", padx=90, pady=20)


button_frame = ctk.CTkFrame(right_frame)
button_frame.pack(fill="x", padx=20, pady=(0, 10))

confirm = ctk.CTkButton(button_frame, text='Loo meelespea', command=lambda: set_event())
confirm.pack(fill="x", padx=10, pady=5)

save_ = ctk.CTkButton(button_frame, text='Salvesta', command=lambda: save())
save_.pack(fill="x", padx=10, pady=5)


def set_event():
    date_gotten = cal.selection_get()
    time_gotten = time_entry.get()
    discord_name = discord_entry.get()
    
    
    formatted_date = date_gotten.strftime("%d/%m/%Y")
    
    if time_gotten:
        text_box.insert(ctk.END, f'\n{discord_name} {formatted_date} {time_gotten}')
        cal.calevent_create(date_gotten, 'reminder2', 'reminder')
        cal.tag_config('reminder', background='red', foreground='yellow')
    else:
        text_box.insert(ctk.END, f'\n{discord_name} {formatted_date}')


def save():
    t = text_box.get(0.0, ctk.END)
    
    jada = t.split("\n")
    
    sonum = jada[0] #value tajken
    
    manydates = (jada[1].strip(" ")).split(" ")
    
    #user_ID = manydates[0] #value tajken
    
    # Create a Workbook object
    wb = Workbook()
    # Remove default worksheets
    wb.Worksheets.Clear()
    # Add a worksheet and name it "Employee"
    sheet = wb.Worksheets.Add("kalender")
    
    file_list = []
    
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):           
            file_list.append(os.path.basename(path).split('/')[-1])
    
    if (manydates[0]) + ".xlsx" not in file_list:
        
        row_inital = 1    
        lisa(row_inital,".",".",".", manydates[0], sheet, wb)
        save()
    
    #del manydates[0]
    #print(manydates)
    uusjada = []
    for liige in manydates[1:]:
        uusjada.append(time_convert(liige))
    print(uusjada)
    print(sonum)
    
    if (manydates[0]) + ".xlsx" in file_list:
        df = pd.read_excel(os.path.join(dir_path, manydates[0]) + ".xlsx", header=None)  # Read without headers to get raw data
        wb = Workbook()
        wb.LoadFromFile("info/"+ manydates[0] +".xlsx")
        sheet = wb.Worksheets["kalender"]
        
        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
        for info in matrix:
            if info[1] == ".":
                row_inital = matrix.index(info) + 1
                lisa(row_inital, uusjada[0], uusjada[1], jada[0], manydates[0],sheet, wb)
                lisa((row_inital+1),".",".",".", manydates[0], sheet, wb)
                #print(matrix)
    
    
    
    
    
    text_box.delete(1.0, ctk.END)

root.title("Weekly")

root.after(0, check)

root.mainloop()



