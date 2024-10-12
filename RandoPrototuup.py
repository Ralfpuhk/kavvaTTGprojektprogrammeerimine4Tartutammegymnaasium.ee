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

# Setup appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Window setup
root = ctk.CTk()
root.title("Weekly")  # Changed title to "Weekly"
root.geometry("900x700")  # Adjusted window size

# Main frame for layout
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Left frame for Discord name entry and mode switch
left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="y", padx=(0, 10))

# Discord name label and entry
discord_label = ctk.CTkLabel(left_frame, text="Discord ID:")
discord_label.pack(padx=10, pady=(10, 0))

discord_entry = ctk.CTkEntry(left_frame, width=100)  # Increased width significantly
discord_entry.pack(padx=10, pady=(0, 10), expand=True)

# Mode switch
mode_switch = ctk.CTkSwitch(left_frame, text="Light Mode", command=lambda: ctk.set_appearance_mode("Light" if ctk.get_appearance_mode() == "Dark" else "Dark"))
mode_switch.pack(pady=(10, 10))

# Right frame for calendar and other components
right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

# Calendar setup
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
                width=30, height= 30)  # Set a specific width
cal.pack(expand=True, fill="both", padx= 50)  # Added padding

# Time entry setup
time_frame = ctk.CTkFrame(right_frame)
time_frame.pack(pady=(10, 0))  # Positioned below the calendar

time_label = ctk.CTkLabel(time_frame, text="Kell: ")
time_label.pack(side="left")

time_entry = ctk.CTkEntry(time_frame, width=60)  # Increased width significantly
time_entry.pack(side="left", padx=(0, 10))  # Add padding to the right

# Set the entry box to be empty
time_entry.delete(0, ctk.END)  # Make sure it is empty

# Textbox setup (further reduced size)
text_box = scrolledtext.ScrolledText(right_frame, width=70, height=10, wrap='word')  # Reduced size again
text_box.pack(expand= True, fill="both", padx=90, pady=20)  # Positioned at the bottom

# Buttons
button_frame = ctk.CTkFrame(right_frame)
button_frame.pack(fill="x", padx=20, pady=(0, 10))

confirm = ctk.CTkButton(button_frame, text='Loo meelespea', command=lambda: set_event())
confirm.pack(fill="x", padx=10, pady=5)

save_ = ctk.CTkButton(button_frame, text='Salvesta', command=lambda: save())
save_.pack(fill="x", padx=10, pady=5)

# Highlight date
def set_event():
    date_gotten = cal.selection_get()
    time_gotten = time_entry.get()
    discord_name = discord_entry.get()
    
    # Format the date to dd-mm-yyyy
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

# Sets time as window title
def time_set():
    root.title(time.strftime('%c'))
    root.after(1000, time_set)

# Initial time setup
time_set()

root.mainloop()
