# TÖÖTAV PROTOTÜÜP
# Meelespea loomiseks pead vajutama kuupäeva peale ning sisestama kellaaja.
# Kellaaeg tuleb sisestada formaadis HH:MM nt 12:29 .
# Kui kuupäev ja kellaaeg on valitud, vajuta "Loo meelespea", kirjuta ning vajuta "Salvesta".
# Salvestamine appendib Discord ID, kuupäeva, kellaaja ning meelespea faili, milleks vaikimisi on fail.txt.
# Kasutajaliidese esteetikat peab veel arendama, aga programm teeb praegu oma töö ära.

from tkcalendar import Calendar
import customtkinter as ctk
import time
import datetime
import tkinter.scrolledtext as scrolledtext


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

time_entry = ctk.CTkEntry(time_frame, width=60)  
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
    
    
    formatted_date = date_gotten.strftime("%d-%m-%Y")
    
    if time_gotten:
        text_box.insert(ctk.END, f'\n{discord_name} {formatted_date} {time_gotten} - ')
        cal.calevent_create(date_gotten, 'reminder2', 'reminder')
        cal.tag_config('reminder', background='red', foreground='yellow')
    else:
        text_box.insert(ctk.END, f'\n{discord_name} {formatted_date} - ')

# Save text
def save():
    t = text_box.get(0.0, ctk.END)
    with open('fail.txt', 'a') as to_save:
        to_save.write(t)

root.mainloop()
