N=int(input())
ans=[1]
for i in range(N):
  print(*ans)
  A=list(ans)
  ans=[1]
  for i in range(len(A)-1):
    ans.append(A[i]+A[i+1])
  ans.append(1)