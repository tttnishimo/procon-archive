N,M=map(int,input().split())
a=[set(list(map(int,input().split()))[1:]) for _ in range(N)]
P,Q=map(int,input().split())
B=set(map(int,input().split()))
ans=0
for i in a:
  if len(i&B)>=Q:
    ans+=1
print(ans)