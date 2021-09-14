N=int(input())
A=list(map(int,input().split()))
C=A[0]
A=[i if i!=-1 else C for i in A]
A.sort()
if A[N-1]==C:
  print('Yes')
else:
  print('No')