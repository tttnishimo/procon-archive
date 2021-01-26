import re
s=input()
t=re.sub('x','',s)
flg=0
for i in range(len(t)//2):
  if t[i]!=t[-i-1]:
    flg=1
if flg==1:
  print(-1)
else:
  a=[]
  tmp=0
  for i in range(len(s)):
    if s[i]=='x':
      tmp+=1
    else:
      a.append(tmp)
      tmp=0
  a.append(tmp)
  a=[abs(a[i]-a[-i-1]) for i in range(len(a)//2)]
  print(sum(a))