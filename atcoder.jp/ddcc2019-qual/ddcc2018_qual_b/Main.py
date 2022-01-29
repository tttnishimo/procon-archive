def is_b(i,j,N):
  if N*3/2-j>=i>=N/2-j and N/2+j>=i>=-N/2+j:
    return True
  else:
    return False
N=int(input())
ans=0
for i in range(N):
  for j in range(N):
    if is_b(i,j,N) and is_b(i+1,j,N) and is_b(i,j+1,N) and is_b(i+1,j+1,N):
      ans+=1
print(ans)