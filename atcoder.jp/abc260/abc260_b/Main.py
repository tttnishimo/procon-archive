N,X,Y,Z=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=[[A[i],B[i],A[i]+B[i],-i-1] for i in range(N)]
ans=[]
a=sorted(a,key=lambda x:(x[0],x[3]),reverse=True)
for i in range(X):
  ans.append(-a.pop(0)[3])
a=sorted(a,key=lambda x:(x[1],x[3]),reverse=True)
for i in range(Y):
  ans.append(-a.pop(0)[3])
a=sorted(a,key=lambda x:(x[2],x[3]),reverse=True)
for i in range(Z):
  ans.append(-a.pop(0)[3])
ans.sort()
print(*ans,sep='\n')