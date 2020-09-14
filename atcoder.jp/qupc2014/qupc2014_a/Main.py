a,b,c,d=map(int,input().split())
e=[list(map(int,input().split())) for _ in range(c)]
ans=[]
for i in range(c):
  e[i].sort(reverse=True)
  ans.append(e[i][b-1])
ans.sort(reverse=True)
print(ans[d-1])