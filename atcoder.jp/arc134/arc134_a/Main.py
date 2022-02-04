N,L,W=map(int,input().split())
A=list(map(int,input().split()))
A.append(L)
ans=(A[0]+W-1)//W
for i in range(N):
  ans+=(A[i+1]-A[i]-1)//W
print(ans)