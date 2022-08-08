N=int(input())
A=list(map(int,input().split()))
ans=[0]
for i in range(N-1):
  ans.append(ans[A[i]-1]+1)
print(ans[-1])