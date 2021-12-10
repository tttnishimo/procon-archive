N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
A=sorted(A,key=lambda x:(x[0],x[1]))
for i in range(N-1):
  if A[i][0]==A[i+1][0]:
    if A[i][2]>A[i+1][1]:
      print('Yes')
      exit()
print('No')