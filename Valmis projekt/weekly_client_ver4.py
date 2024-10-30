# Client
# Tee eraldi kaust programmi jaoks ning tehtud kaustas pane eraldi kaustadesse Host-programm ja Client-programm.
# Host-programm peab töötama koguaeg, et sõnum saadetaks
# Meelespea loomiseks pead vajutama kuupäeva peale ning sisestama kellaaja.
# Kellaaeg tuleb sisestada formaadis HH:MM nt 12:29 voi 01:32
# Kui kuupäev ja kellaaeg on valitud, vajuta "Loo meelespea", siis kirjuta selle kohale oma sonum ning vajuta "Salvesta".
# Salvestamine appendib Discord ID, kuupäeva, kellaaja ning meelespea ning kohandab andmed ja salvestab .xlsx faili.
# NB! Programm peab lahti olema, et see sonumi saadaks Discordi. (discordi server, millesse sonum saadetakse: https://discord.gg/qr4RssDH9J)
# Programm saadab teate minuti jooksul, kuna oleneb programmi avamise ajast -> ei pruugi olla iga minuti alguses.
# Kuidas saada oma discord ID: 
# Vajuta discordis all vasakul nupule "User Settings" -> Vajuta "Advanced" -> Käivita "Developer Mode" -> Mine seadetest välja -> All vasakul vajuta oma discordi profiili peale -> Vajuta "Copy User ID"

port = 54123
IP = "127.0.0.1" # hosti IP. vajadusel muuda host programmi "IPv4" IP-ks. Tee seda ka host programmis. 
#(tootab ainult local networkide peal kuna public server IP maksab raha)

import shutil

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

def file_list_cck():
    file_list = []
    
    for path in os.listdir(dir_name_slash):
        if os.path.isfile(os.path.join(dir_name_slash, path)):           
            file_list.append(os.path.basename(path).split('/')[-1])
    return(file_list)

def lisa(row, input_kuupaev, input_kell, input_sonum, user, sheet, wb):
    
    assignment = [input_kuupaev, input_kell, input_sonum]
    column = ["A", "B", "C"]
    for num in column:
        cell = ("%s%s" % (num, row))
        sheet.Range[cell].Text = assignment[column.index(num)]
        
    path = ("info/"+ user +".xlsx")
    wb.SaveToFile(path, FileFormat.Version2016)
    return


def time_convert(date1):
    print(date1)
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
        if date == "":
            date = "0"
        lias.append(date)
    string = separator.join(lias)
    return(string)
    #print(string)

dir_name_slash = "info/"
dir_name = "info"


def digdin(message, nimi):
    discordWebhook = "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
    discord = Discord(url=discordWebhook)#

    discord.post(content = ("<@"+(str(nimi[:len(nimi)-5]))+">" + " has set the following notification to go off now: \n" + str(message)))

def recieve_xslx(s, flyname):
    
    flypath = os.path.join(dir_name, flyname)  
    print(flypath)
    
    total_bytes = 0
    
    with open(flypath, 'wb') as f:
        while True:
            data = s.recv(1024) 
            if data == b"EOF": 
                print("breaking")
                break
            f.write(data)
            bytess = len(data)
            #print(bytess)
            if bytess < 1024:
                s.sendall("confirmation".encode("utf-8")) #ma leidsin probleemi :)
                
    print("received")

def send_xslx(send11, s):
    
    
    flyfile = os.path.join(dir_name, send11)
    flyname = os.path.basename(flyfile)  

    # Github code :) -> ma eriti ei moista, aga midagi see saadab filei nime pikkuse, et see hiljem suudaks decodeida 
    file_name_bytes = flyname.encode("utf-8")
    s.sendall(len(file_name_bytes).to_bytes(4, 'big'))
    s.sendall(file_name_bytes)

    with open(flyfile, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            s.sendall(data)
    print("File sent successfully.")
    time.sleep(0.5) # igaksjuhuks, et socket katki ei laheks kui funktsiooni liiga palju kasutada jarjest. vist pole vaja, aga las olla


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Weekly")  
root.geometry("900x700")  


main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)


left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="y", padx=(0, 10))


discord_label = ctk.CTkLabel(left_frame, text="Discord ID:",font= ("Arial", 14))
discord_label.pack(padx=10, pady=(10, 0))

discord_entry = ctk.CTkEntry(left_frame, width=100)
discord_entry.pack(padx=10, pady=(0, 10), expand=True)


        


mode_switch = ctk.CTkSwitch(left_frame, text="Light Mode",font= ("Arial", 14), command=lambda: ctk.set_appearance_mode("Light" if ctk.get_appearance_mode() == "Dark" else "Dark"))
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

time_label = ctk.CTkLabel(time_frame, text="Kell: ",font= ("Arial", 14))
time_label.pack(side="left")

time_entry = ctk.CTkEntry(time_frame, width=60)  
time_entry.pack(side="left", padx=(0, 10))

vale_label = ctk.CTkLabel(time_frame, text="VALE VORMISTUS! ", font= ("Arial", 14))

vale_label.pack(side="right")
vale_label.pack_forget()

# ////////////////////////////////////////

aeg_label = ctk.CTkLabel(time_frame, text="Uudiste aeg:",font= ("Arial", 14))
aeg_label.pack(side="left", padx=(0, 5))  


aeg_entry = ctk.CTkEntry(time_frame, width=60)
aeg_entry.pack(side="left", padx=0, pady=(0, 10))  

aeg_entry.pack_forget()
aeg_label.pack_forget()



def toggle_uudised():
    if uudised_checkbox.get():
        aeg_label.pack(side = "left", padx=0, pady=(0, 0))
        aeg_entry.pack(side = "left", padx=5, pady=(0, 5))
        
    else:
        aeg_entry.pack_forget()
        aeg_label.pack_forget()


time_entry.delete(0, ctk.END)  

uudised_checkbox = ctk.CTkCheckBox(left_frame, text="Viimatised uudised",font= ("Arial", 14), command = toggle_uudised)
uudised_checkbox.pack(padx=10, pady=(0, 10))


text_box = scrolledtext.ScrolledText(right_frame, width=70, height=10, wrap='word')  
text_box.pack(expand= True, fill="both", padx=90, pady=20)



button_frame = ctk.CTkFrame(right_frame)
button_frame.pack(fill="x", padx=20, pady=(0, 10))

confirm = ctk.CTkButton(button_frame, text='Loo meelespea',font= ("Arial", 14), command=lambda: set_event())
confirm.pack(fill="x", padx=10, pady=5)

save_ = ctk.CTkButton(button_frame, text='Salvesta',font= ("Arial", 14), command=lambda: save())
save_.pack(fill="x", padx=10, pady=5)











def set_event():
    
    count1 = 0
    count2 = 0
    news_get = str(aeg_entry.get())

    
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


    
    
    for a in time_gotten:
        if (a.isalpha()) == True:
            count1 += 1
            
    for a in news_get:
        if (a.isalpha()) == True:
            count2 += 1
            
    if count1 or count2 > 0:
        vale_label.pack(side = "right", padx=0, pady=(0, 0))
        text_box.delete(1.0, ctk.END)

    else:
        vale_label.pack_forget()
    
    
    
def save():
    
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{dir_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    news_get = str(aeg_entry.get())
    if news_get != "" and news_get != ".":
        news_get = time_convert(str(news_get))
    if news_get == "":
        news_get = "."
#     print(news_get)
    s = socket.socket()

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
    
    #del manydates[0]
    #print(manydates)
    uusjada = []
    for liige in manydates[1:]:
        uusjada.append(time_convert(liige))
        
#     print(manydates)
#     print(uusjada)
#     print(sonum)

    s.connect((IP, port))
    
    s.sendall((manydates[0]).encode())
#     print(manydates[0] + "!!!!")
    
    #     host stuff -> saadab tagasi kas file on olemas
    
    file_confirmation = s.recv(1024).decode("utf-8")
    
#     print(file_confirmation)
    
    if file_confirmation == "0":
        print("no excel found from host. creating new file.")
        if (manydates[0]) + ".xlsx" not in file_list_cck():
            
            row_inital = 1    
            lisa(row_inital,".",".",".", manydates[0], sheet, wb)            
            time.sleep(0.5)
            
        file_list_cck()
        uusjada = []
        for liige in manydates[1:]:
            uusjada.append(time_convert(liige))
        print(uusjada)
        print(sonum)
        
        if (manydates[0]) + ".xlsx" in file_list_cck():
            df = pd.read_excel(os.path.join(dir_name_slash, manydates[0]) + ".xlsx", header=None)  # pandas loeb excel file, et meil oleks midagi jadaks muuta, kuna python ise ei suuda vist xlsx faili lugeda
            wb = Workbook()
            wb.LoadFromFile("info/"+ manydates[0] +".xlsx")
            sheet = wb.Worksheets["kalender"]
            
            values = df.values.flatten()
            num_cols = 3
            matrix = values.reshape(-1, num_cols).tolist()
            for info in matrix:
                if info[0] == ".":
                    row_inital = matrix.index(info) + 1
                    lisa(row_inital, uusjada[0], uusjada[1], jada[0], manydates[0],sheet, wb)
                    lisa((row_inital+1),".",news_get,".", manydates[0], sheet, wb)
                    #print(matrix)
                    
        send_xslx(((manydates[0]) + ".xlsx"), s)
    
    elif file_confirmation == "1":
        print("recieving excel form host")


        recieve_xslx(s, ((manydates[0]) + ".xlsx"))
        
        
        df = pd.read_excel(os.path.join((dir_name_slash + manydates[0])) + ".xlsx", header=None)
        wb = Workbook()
        wb.LoadFromFile("info/"+ manydates[0] +".xlsx")
        sheet = wb.Worksheets["kalender"]
        
        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
        for info in matrix:
            
            if info[0] == ".":
                row_inital = matrix.index(info) + 1
                print(row_inital)
                lisa(row_inital, uusjada[0], uusjada[1], jada[0], manydates[0],sheet, wb)
                lisa((row_inital+1),".",news_get,".", manydates[0], sheet, wb)
                #print(matrix)
        send_xslx(((manydates[0]) + ".xlsx"), s)
        
    s.close()
    
    text_box.delete(1.0, ctk.END)
    
    try:
        shutil.rmtree("info")
        print("Info kaust kustutatud")
    except OSError as e:
        print("ei ole olemas")
    
def on_closing():
    root.destroy()    
    
root.title("Weekly")

root.mainloop()

