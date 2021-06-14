import datetime
#or
from datetime import datetime

now = datetime.now()
print(now)
year = now.strftime("%Y")
print("Year:", year)
month=now.strftime("%m")
print("month:",month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print ("time:", time)
mytime = now.strftime("%d-%m-%y")
print(mytime)
date_time = now.strftime("%d/%m/%Y-%H:%M:%S")
print(" DATE and TIME",date_time)

