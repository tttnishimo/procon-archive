N=int(input())
A=[input() for _ in range(N)]
for i in range(N):
  for j in range(N):
    if A[i][j]=='-' or A[i][j]==A[j][i]=='D' or (A[i][j]=='W' and A[j][i]=='L') or (A[i][j]=='L' and A[j][i]=='W'):
      continue
    else:
      print('incorrect')
      exit()
print('correct')