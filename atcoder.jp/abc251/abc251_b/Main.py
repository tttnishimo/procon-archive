N,W=map(int,input().split())
A=list(map(int,input().split()))
ans=set()
for i in range(N):
  for j in range(i,N):
    for k in range(j,N):
      if i==j:
        if j==k:
          if A[i]<=W:
            ans.add(A[i])
      elif j==k:
        if A[i]+A[j]<=W:
          ans.add(A[i]+A[j])
      else:
        if A[i]+A[j]+A[k]<=W:
          ans.add(A[i]+A[j]+A[k])
print(len(ans))