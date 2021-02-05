import datetime as dt
while True:
  s=input()
  if s=='0':
    break
  y=int(s[:s.index('/')])
  t=(y-1001)//2000
  y-=t*2000
  s=str(y)+s[s.index('/'):]
  d=dt.datetime.strptime(s,'%Y/%m/%d %H:%M:%S')
  n=int(input(),2)
  d=d+dt.timedelta(seconds=n)
  print(str(d.year+2000*t)+'/'+'0'*(1-d.month//10)+str(d.month)+'/'+'0'*(1-d.day//10)+str(d.day),d.time())