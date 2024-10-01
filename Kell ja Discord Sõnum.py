import time
import datetime
from discordwebhook import Discord

# discord boti webhook: "https://discord.com/api/webhooks/1285532569252663329/Exwjdv428I8ev5W3gXDqowPnWX7c2cybHOpn0sGB4RowZha_XyIF-FzqvbkQtpaQ4XLx"
# discord bot appi token: "MTI5MDYwMDk0NTUyODYwMjY4NQ.GXN744.rSDaZvKUJdHKbwsikio67O8QFo4alMfqdABPYg"

discordWebhook = input("Enter your discord bots webhook: ")
discord = Discord(url=discordWebhook)

i = 0
while i == 0:
    current_time = datetime.datetime.now()		#current everything (year-month-day-hour-minute)
    MONTH = datetime.date.today().month		# current month
    DAY = datetime.date.today().day		# current day
    HOUR = datetime.datetime.now().hour   # current hour
    MINUTE = datetime.datetime.now().minute #  current minute
    
    print(str(HOUR) + ":" + str(MINUTE))
    time.sleep(1)
    
    if MINUTE == 52:
        discord.post(content="opa")

    

    









