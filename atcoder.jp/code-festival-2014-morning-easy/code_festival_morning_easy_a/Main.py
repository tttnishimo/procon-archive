n=int(input())
a=list(map(int,input().split()))
tmp=0
for i in range(n-1):
  tmp+=a[i+1]-a[i]
print(tmp/(n-1))