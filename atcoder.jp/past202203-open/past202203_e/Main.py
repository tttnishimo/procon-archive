import datetime as dt
import collections
S=input()
s=dt.datetime.strptime(S,'%Y/%m/%d')
td_d=dt.timedelta(days=1)
while True:
  S=s.strftime('%Y/%m/%d')
  c=collections.Counter(S)
  if len(c)<=3:
    print(S)
    exit()
  s+=td_d