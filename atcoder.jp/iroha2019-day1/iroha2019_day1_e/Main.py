N,A,B=map(int,input().split())
D=[]
if B:
  D=list(map(int,input().split()))
  D.sort()
D=[0]+D+[N+1]
ans=N-B
for i in range(B+1):
  ans-=(D[i+1]-D[i]-1)//A
print(ans)