n=int(input())
a=list(map(int,input().split()))
a.sort()
b=[0]*(a[-1]+1)
ans=0
for i in range(n):
  for j in range(a[i],a[-1]+1,a[i]):
    b[j]+=1
print(sum(1 if b[i]==1 else 0 for i in a))