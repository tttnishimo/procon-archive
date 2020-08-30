n=int(input())
ans=0
for _ in range(n):
  a,b=map(int,input().split())
  ans+=a*b*1.05
print(int(ans))