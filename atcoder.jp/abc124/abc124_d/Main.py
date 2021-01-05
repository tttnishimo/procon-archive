import itertools
n,k=map(int,input().split())
s=input()
flg=1
a=[]
if s[0]=='0':
  a.append(0)
for i in range(n-1):
  if s[i]==s[i+1]:
    flg+=1
  else:
    a.append(flg)
    flg=1
a.append(flg)
if s[-1]=='0':
  a.append(0)

if len(a)>=2*k+1:
  a=list(itertools.accumulate(a))
  a.insert(0,0)
  b=[a[2*i+2*k+1]-a[2*i] for i in range(len(a)//2-k)]
  print(max(b))
else:
  print(sum(a))