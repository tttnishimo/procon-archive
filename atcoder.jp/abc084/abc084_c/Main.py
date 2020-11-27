n=int(input())
a=[list(map(int,input().split())) for _ in range(n-1)]
for i in range(n-1):
  t=0
  for j in range(i,n-1):
    if t<a[j][1]:
      t=a[j][0]+a[j][1]
    else:
      t=a[j][0]-(-(t-a[j][1])//a[j][2])*a[j][2]+a[j][1]
  print(t)
print(0)