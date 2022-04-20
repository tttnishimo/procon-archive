import bisect
N=int(input())
A=list(map(int,input().split()))
ma=max(A)
B=[[] for _ in range(ma+1)]
for i in range(N):
  B[A[i]].append(i)
for _ in range(int(input())):
  L,R,X=map(int,input().split())
  if X>ma:
    print(0)
    continue
  print(bisect.bisect_right(B[X],R-1)-bisect.bisect_left(B[X],L-1))