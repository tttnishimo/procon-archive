import datetime
s = input()
d=datetime.datetime.strptime(s,"%Y/%m/%d")
while d.year<=2999:
  if (d.year/d.month/d.day).is_integer():
    break
  d+=datetime.timedelta(days=1)
print(d.strftime("%Y/%m/%d"))