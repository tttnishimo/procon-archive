N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
if M>N:
  print('NO')
else:
  flg=0
  for i in range(M):
    if B[i]>A[i]:
      flg=1
  if flg==1:
    print('NO')
  else:
    print('YES')