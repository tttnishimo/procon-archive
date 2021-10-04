import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
B.sort()
ans=0
for i in A:
  ans+=M-bisect.bisect_left(B,i)
print(ans)