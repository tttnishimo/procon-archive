D=int(input())
H=[list(map(int,input().split())) for _ in range(int(input()))]
A=[0]*(D+2)
for i,j in H:
  A[i]+=1
  A[j+1]-=1
for i in range(D+1):
  A[i+1]+=A[i]
print(*A[1:-1],sep='\n')