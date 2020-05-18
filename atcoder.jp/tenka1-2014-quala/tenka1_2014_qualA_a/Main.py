n=1000
a=[]
for i in range(1,n+1):
  a.append(str(i))
a.sort()
for i in range(n):
  print(a[i])