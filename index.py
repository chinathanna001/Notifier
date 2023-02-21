import sqlite3
import datetime
import time

# Connect to SQLite database
conn = sqlite3.connect('index.db')
c = conn.cursor()

while True:
    # Retrieve time and message from database
    c.execute('SELECT isdaily, time, date, message FROM reminders')
    reminders = c.fetchall()

    # Check if any reminders match the current time
    now = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M')
    nowd = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%D')
    for reminder in reminders:
        if reminder[0] == 1:
            if reminder[1] == now:
                print(reminder[3])
        else:
            if reminder[1] == now & reminder[2] == nowd:
                print(remainder[3])


    # Wait for 1 minute before checking again
    time.sleep(60)

# Close database connection
conn.close()
