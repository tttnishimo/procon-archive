N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=list(map(int,input().split()))
E=[]
F=[]
for i in range(N):
  for j in range(N):
    E.append(A[i]+B[j])
    F.append(C[i]+D[j])
F=set(F)
for e in E:
  if K-e in F:
    print('Yes')
    exit()
print('No')