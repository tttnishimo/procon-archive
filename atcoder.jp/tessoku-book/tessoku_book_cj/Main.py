import bisect
N=int(input())
A=list(map(int,input().split()))
A.sort()
for _ in range(int(input())):
  X=int(input())
  print(bisect.bisect_left(A,X))