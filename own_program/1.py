import re
import datetime


a = "Біологія+1легені"

match = re.match(r"([^\+\d]+)\+(\d+)(.*)", a)

name = match.group(1).strip()
date = int(match.group(2))
other = match.group(3).strip()

new_date = datetime.date.today() + datetime.timedelta(days=date)
new_date1 = new_date.strftime("%d.%m")

print(name)
print(date)
print(other)
print(new_date1)