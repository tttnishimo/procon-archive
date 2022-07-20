N,X,Y=map(int,input().split())
ans=[[1,0]]
for i in range(N-1):
  ans.append([0,0])
for i in range(N-1):
  x=ans[i][0]
  ans[i]=[0,ans[i][1]+x*X]
  ans[i+1][0]+=x
  y=ans[i][1]
  ans[i]=[0,0]
  ans[i+1][0]+=y
  ans[i+1][1]+=y*Y
print(ans[-1][1])