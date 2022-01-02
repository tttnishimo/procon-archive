import bisect
N=int(input())
A=list(map(int,input().split()))
A.sort()
for _ in range(int(input())):
  b=int(input())
  c=bisect.bisect(A,b)
  if c==0:
    print(A[0]-b)
  elif c==N:
    print(b-A[-1])
  else:
    print(min(A[c]-b,b-A[c-1]))