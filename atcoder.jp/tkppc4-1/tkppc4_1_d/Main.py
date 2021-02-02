n=int(input())
a=list(map(int,input().split()))
f=0
b=1
for i in range(1,n):
  if a[i]>a[i-1] and f!=1:
    f=1
    b+=1
  elif a[i]<a[i-1] and f!=-1:
    f=-1
    b+=1
if a.count(a[0])==n:
  b=0
print(b)