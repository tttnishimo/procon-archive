n=int(input())
a=list(map(int,input().split()))
ans={}
for i in a:
  while i%2==0:
    i//=2
  if ans.get(i,0)==0:
    ans[i]=1
print(len(ans))