import time
import datetime
from discordwebhook import Discord




i = 0
while i == 0:
    current_time = datetime.datetime.now()
    DATE = datetime.date.today().day
    HOUR = datetime.datetime.now().hour   # the current hour
    MINUTE = datetime.datetime.now().minute # the current minute
    
    print(str(HOUR) + ":" + str(MINUTE))
    time.sleep(1)
    if MINUTE == 0:
        discord = Discord(url="https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx")
        discord.post(content="Ärka yles")
    

    









