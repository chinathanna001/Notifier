import sqlite3
import datetime
import time


conn = sqlite3.connect('index.db')
c = conn.cursor()

while True:
    c.execute('SELECT Time, Day, Period FROM TimeTable')
    time = c.fetchall()

    now = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M')
    nowd = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%A')
    for TimeTable in time:
        if TimeTable[0] == now & TimeTable[1] == nowd:
            print(TimeTable[2])

    time.sleep(60)


conn.close()