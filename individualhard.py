import datetime
from math import floor
now = datetime.datetime.now()
m = float(now.minute) + float(now.second/60)
ugol = m/5*30
print(str(now.hour) + " час " + str(now.minute) + " минут")
print(str(floor(ugol)) + " Угол")