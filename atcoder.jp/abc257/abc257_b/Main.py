N,Q,K=map(int,input().split())
A=list(map(int,input().split()))
A.append(N+1)
L=list(map(int,input().split()))
for i in L:
  if A[i-1]+1!=A[i]:
    A[i-1]+=1
print(*A[:-1])