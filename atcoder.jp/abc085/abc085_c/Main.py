n,k = map(int, input().split())
a = [-1,-1,-1]
for i in range(n+1):
  for j in range(n-i+1):
    if i*10000+j*5000+(n-i-j)*1000 == k:
        a = [i,j,n-i-j]
print(*a)