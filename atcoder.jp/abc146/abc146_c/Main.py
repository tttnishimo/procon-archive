a,b,x=map(int,input().split())
n=1
while 10*n*a+b*(len(str(n))+1)<x:
  n*=10
ans=(x-b*len(str(n)))//a
if len(str(ans))>len(str(n)):
  ans-=1
if ans>=10**9:
  print(1000000000)
elif ans<=0:
  print(0)
else:
  print(ans)