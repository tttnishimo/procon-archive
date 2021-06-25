n,k=map(int,input().split())
n-=2
ans=[]
for i in range(1,12):
  t=0
  for j in range(1,6):
    if (((i-1)*7+j)*9+72)%11==k:
      t+=1
  ans.append(t)
print(sum(ans)*(n//11)+sum(ans[:n%11]))
