H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
for i in range(H-1):
  for j in range(i,H):
    for k in range(W-1):
      for l in range(k,W):
        if A[i][k]+A[j][l]>A[i][l]+A[j][k]:
          print('No')
          exit()
print('Yes')