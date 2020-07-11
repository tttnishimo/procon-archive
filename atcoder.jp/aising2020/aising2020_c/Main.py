n=int(input())
a=[0]*(10**4)
for i in range(1,10**2+1):
  for j in range(1,10**2+1):
    for k in range(1,10**2+1):
      b=i**2+j**2+k**2+i*j+j*k+k*i-1
      if b<=10**4-1:
        a[b]+=1
for i in range(n):
  print(a[i])