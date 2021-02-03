from datetime import date
ma,da=map(int,input().split())
mb,db=map(int,input().split())
print((date(2012,mb,db)-date(2012,ma,da)).days)