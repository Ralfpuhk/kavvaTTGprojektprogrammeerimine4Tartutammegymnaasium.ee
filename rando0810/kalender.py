from tkcalendar import Calendar, DateEntry
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
def button_callback():
    kp = cal.selection_get()
    print(kp)
def mainF():
    global cal
    def getDate():
        date=cal.get_date()
        print(date)
    cal.pack(pady=20, padx=20)
root = ctk.CTk()
root.title("Weekly")
root.geometry("550x400")
raam = ctk.CTkFrame(root)
raam.pack(fill="both", padx=10, pady=10, expand=True)
button = ctk.CTkButton(root, text="Vali see kuupäev", command=button_callback)
button.pack(side = ctk.LEFT, expand= True, padx=20, pady=20)

style = ttk.Style(root)
style.theme_use("default")

cal = Calendar(raam, selectmode='day', locale='et', disabledforeground='red',
               cursor="hand2", background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],
               selectbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1])
cal.pack(side = ctk.RIGHT, fill = "both",expand=True, padx=10, pady=10)
cal=Calendar(root,selectmode="day",date_pattern="dd-mm-y")
root.mainloop()