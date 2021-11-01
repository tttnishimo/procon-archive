N,M=map(int,input().split())
A=list(map(int,input().split()))
B=set(map(int,input().split()))
ans=0
for i in B:
  ans+=A.count(i)
print(ans)