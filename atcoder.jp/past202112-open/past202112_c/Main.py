N=int(input())
al=['A','B','C','D','E','F']
ans=[0,0,0,0,0,0]
for i in range(N):
  p,v=map(str,input().split())
  if v=='AC' and ans[al.index(p)]==0:
    ans[al.index(p)]=i+1
print(*ans,sep='\n')