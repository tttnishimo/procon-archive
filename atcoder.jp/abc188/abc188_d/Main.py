n,C=map(int,input().split())
a=[]
for _ in range(n):
  b,c,d=map(int,input().split())
  a.append([b,d])
  a.append([c+1,-d])
a.sort()
ans,tmp=0,0
for i in range(len(a)-1):
  tmp+=a[i][1]
  ans+=min(tmp,C)*(a[i+1][0]-a[i][0])
print(ans)