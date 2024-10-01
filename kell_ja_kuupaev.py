import time
import datetime

i = 0
while i == 0:
    current_time = datetime.datetime.now()
    day = datetime.date.today().day
    month = datetime.date.today().month
    HOUR = datetime.datetime.now().hour   # the current hour
    MINUTE = datetime.datetime.now().minute # the current minute
    
    print(str(HOUR) + ":" + str(MINUTE))
    time.sleep(1)
    print(str(day) + "." + str(month))
    

    








