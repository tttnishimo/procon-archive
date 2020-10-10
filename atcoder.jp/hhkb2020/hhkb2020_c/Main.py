n=int(input())
a=list(map(int,input().split()))
ans=0
d={}
for i in a:
  if d.get(i,0)==0:
    d[i]=1
    while d.get(ans,0)==1:
      ans+=1
  print(ans)