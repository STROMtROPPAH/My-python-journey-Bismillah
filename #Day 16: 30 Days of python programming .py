from datetime import datetime

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp

print(day, month, year, hour, minute)
print("time stamp: ", timestamp)


from datetime import datetime

now = datetime.now()
formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted)

from datetime import datetime

date_string = "5 December, 2019"
parsed = datetime.strptime(date_string, "%d %B, %Y")
print(parsed)

