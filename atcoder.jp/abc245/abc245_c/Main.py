N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=[True]
b=[True]
for i in range(1,N):
  if (a[i-1] and abs(A[i]-A[i-1])<=K) or (b[i-1] and abs(A[i]-B[i-1])<=K):
    a.append(True)
  else:
    a.append(False)
  if (a[i-1] and abs(B[i]-A[i-1])<=K) or (b[i-1] and abs(B[i]-B[i-1])<=K):
    b.append(True)
  else:
    b.append(False)
if a[-1] or b[-1]:
  print('Yes')
else:
  print('No')