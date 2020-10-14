n=int(input())
a=list(map(int,input().split()))
t=10**9
b=0
for i in range(n):
  if abs(t)>abs(a[i]):
    t=abs(a[i])
  if a[i]<0:
    b+=1
  a[i]=abs(a[i])
if b%2==0:
  print(sum(a))
else:
  print(sum(a)-2*t)