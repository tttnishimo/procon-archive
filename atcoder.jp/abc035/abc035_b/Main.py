s=input()
a,b,c=0,0,0
for i in range(len(s)):
  if s[i]=='U':
    a+=1
  elif s[i]=='D':
    a-=1
  elif s[i]=='L':
    b+=1
  elif s[i]=='R':
    b-=1
  else:
    c+=1
if input()=='1':
  print(abs(a)+abs(b)+c)
else:
  ans=abs(a)+abs(b)-c
  if ans>=0:
    print(ans)
  elif ans%2==0:
    print(0)
  else:
    print(1)