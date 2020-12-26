n=int(input())
a=list(map(int,input().split()))
ans=0
b=[0,0]
t=a[0]
for i in a:
  if i>t:
    b[0]=1
    if b[1]==1:
      b[1]=0
      ans+=1
  elif i<t:
    b[1]=1
    if b[0]==1:
      b[0]=0
      ans+=1
  t=i
if ans==0:
  print(0)
else:
  print(ans+2)