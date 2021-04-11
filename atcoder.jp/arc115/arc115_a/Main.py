n,m=map(int,input().split())
ans=[0,0]
for _ in range(n):
  if input().count('1')%2==0:
    ans[0]+=1
  else:
    ans[1]+=1
print(ans[0]*ans[1])