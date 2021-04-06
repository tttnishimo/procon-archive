import datetime
n=int(input())
flg=0
ans=0
a=[1 if i%7==0 or i%7==6 else 0 for i in range(366)]
d1=datetime.date(2012,1,1)
for i in range(n):
  s=input()
  d=datetime.date(2012,int(s[:s.index('/')]),int(s[s.index('/')+1:]))
  a[(d-d1).days]+=1
for i in range(366):
  while a[i]>1 and 0 in a[i+1:]:
    a[i]-=1
    a[a[i+1:].index(0)+i+1]+=1
for i in range(366):
  if a[i]>=1:
    flg+=1
  else:
    ans=max(ans,flg)
    flg=0
ans=max(ans,flg)
print(ans)