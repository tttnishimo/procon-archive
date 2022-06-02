ans=0
for _ in range(int(input())):
  P,Q=map(int,input().split())
  ans+=Q/P
print(ans)