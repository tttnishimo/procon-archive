n=int(input())
a=[]
b=[]
for i in range(n):
  tmpa,tmpb=map(int,input().split())
  a.append(tmpa)
  b.append(tmpb)
if n%2==1:
  a.sort()
  b.sort()
  print(b[n//2]-a[n//2]+1)
else:
  a.sort()
  b.sort()
  tmp=(b[n//2-1]+b[n//2])/2 - (a[n//2-1]+a[n//2])/2
  if tmp.is_integer():
    print(int(tmp)*2+1)
  else:
    print(int(tmp+0.5)*2)