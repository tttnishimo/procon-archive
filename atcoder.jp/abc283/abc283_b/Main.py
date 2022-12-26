N=int(input())
A=list(map(int,input().split()))
for _ in range(int(input())):
  Q=list(map(int,input().split()))
  if Q[0]==1:
    A[Q[1]-1]=Q[2]
  else:
    print(A[Q[1]-1])