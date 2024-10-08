import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkcalendar import Calendar
import time
import datetime

# window setup
root = tk.Tk()
# calendar
today = datetime.date.today()
mindate = datetime.date(year=2000, month=1, day=1)
maxdate = today + datetime.timedelta(days=365)
CALENDAR = Calendar(root,
      font="Arial 14",
      selectmode='day',
      locale='et',
      mindate=mindate,
      maxdate=maxdate,
      disabledforeground='red',
      cursor="hand1",
      year=int(time.strftime('%Y')),
      month=int(time.strftime('%m')),
      day=int(time.strftime('%d')))
CALENDAR.pack(fill="both", expand=True)

# textbox
text_box = scrolledtext.ScrolledText(root,width=10,height=10,wrap='word')
text_box.pack(fill="x",expand=True)

# highlight date
def set_event():
    date_gotten = CALENDAR.selection_get()
    text_box.insert(tk.END,'\n'+str(date_gotten)+' - ')
    CALENDAR.calevent_create(date_gotten,'reminder2','reminder')
    CALENDAR.tag_config('reminder',background='red', foreground='yellow')

# un-highlight date
def delete_event():
    date_gotten = CALENDAR.selection_get()
    CALENDAR.tag_config(date_gotten,background='blue', foreground='white')

# save text
def save():
    t = text_box.get(0.0,tk.END)
    to_save = open('fail.txt','w')
    to_save.write(t)
    to_save.close()

# load text
def load():
    to_load = open('fail.txt','r').read()
    text_box.delete(0.0,tk.END)
    text_box.insert(0.0,to_load)

# sets time as window title
def time_set():
    root.title(time.strftime('%c'))
    root.after(10, time_set)

# buttons
confirm = tk.Button(root,text='Create Event',command=set_event)
confirm.pack(fill="x", expand=True)
delete  = tk.Button(root,text='Delete Event',command=delete_event)
delete.pack (fill="x", expand=True)
save_   = tk.Button(root,text='Save'        ,command=save)
save_.pack  (fill="x", expand=True)
load_   = tk.Button(root,text='Load'        ,command=load)
load_.pack  (fill="x", expand=True)

load()
time_set()
root.mainloop()