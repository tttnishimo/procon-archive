a=[1,1]
for i in range(100):
  a.append(a[-2]+a[-1])
for _ in range(int(input())):
  X=int(input())
  b=10**18
  for i in range(100):
    if (X-a[i])%a[i+1]==0:
      b=max(min((X-a[i])//a[i+1],b),1)
  print(1,b)