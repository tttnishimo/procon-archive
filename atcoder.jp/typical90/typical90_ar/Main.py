N,Q=map(int,input().split())
A=list(map(int,input().split()))
flg=0
for _ in range(Q):
  T,x,y=map(int,input().split())
  if T==1:
    A[x-1-flg],A[y-1-flg]=A[y-1-flg],A[x-1-flg]
  elif T==2:
    flg+=1
    flg%=N
  else:
    print(A[x-1-flg])