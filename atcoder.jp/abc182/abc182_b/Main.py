n=int(input())
a=list(map(int,input().split()))
ans=[0,0]
for i in range(2,1001):
  tmp=0
  for j in a:
    if j%i==0:
      tmp+=1
  if ans[1]<=tmp:
    ans[0]=i
    ans[1]=tmp
print(ans[0])