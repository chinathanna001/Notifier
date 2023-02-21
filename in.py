from datetime import datetime
import pytz
now = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%A')

print(now)