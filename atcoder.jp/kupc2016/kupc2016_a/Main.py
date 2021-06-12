N,A,B=map(int,input().split())
t=[int(input()) for _ in range(N)]
ans=0
for i in t:
  if A<=i<B:
    continue
  ans+=1
print(ans)