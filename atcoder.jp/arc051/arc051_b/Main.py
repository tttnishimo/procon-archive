n=int(input())
a=[1,2]
for i in range(40):
  a.append(a[-1]+a[-2])
print(a[n],a[n-1])