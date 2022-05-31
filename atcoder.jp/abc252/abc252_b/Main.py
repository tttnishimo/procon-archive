N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=max(A)
for i in range(N):
  if A[i]==a and (i+1 in B):
    print('Yes')
    exit()
print('No')