import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=[A[i]-i for i in range(N)]
for _ in range(Q):
  K=int(input())
  ans=K+bisect.bisect_right(B,K)
  print(ans)