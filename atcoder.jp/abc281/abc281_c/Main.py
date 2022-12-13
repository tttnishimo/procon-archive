N,T=map(int,input().split())
A=list(map(int,input().split()))
T-=T//sum(A)*sum(A)
for i in range(N):
  if A[i]>T:
    print(i+1,T)
    exit()
  else:
    T-=A[i]