import bisect
N=int(input())
A=list(map(int,input().split()))
A.sort()
B=[0]
for a in A:
  B.append(B[-1]+a)
B=B[1:]
for _ in range(int(input())):
  X=int(input())
  print(bisect.bisect(B,X))