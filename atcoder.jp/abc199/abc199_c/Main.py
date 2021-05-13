N=int(input())
S=input()
flg=False
a=[i for i in range(2*N+1)]
for _ in range(int(input())):
  T,A,B=map(int,input().split())
  if T==1:
    if flg:
      A=(A+N)%(2*N) if A!=N else 2*N
      B=(B+N)%(2*N) if B!=N else 2*N
    a[A],a[B]=a[B],a[A]
  else:
    flg=not flg
t=''
if not flg:
  for i in range(1,2*N+1):
    t+=S[a[i]-1]
else:
  for i in range(N+1,2*N+1):
    t+=S[a[i]-1]
  for i in range(1,N+1):
    t+=S[a[i]-1]
print(t)