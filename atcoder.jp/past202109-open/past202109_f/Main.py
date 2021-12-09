N=int(input())
S=input()
A=[i+1 for i in range(N)]
if S.count('0')==1:
  print(-1)
else:
  f='0'
  l=-1
  for i in range(N):
    if S[i]==f=='0':
      f=A[i]
      l=i
    elif S[i]=='0':
      A[i],f=f,A[i]
  if l!=-1:
    A[l]=f
  print(*A)