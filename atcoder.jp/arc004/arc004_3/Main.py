a,b=map(int,input().split('/'))
n=2*a//b
ans=[]
for i in range(2):
  n+=i
  m=n*(n+1)//2-n*a//b
  if (n*a)%b==0 and n:
    ans.append([n,int(m)])
if ans==[]:
  print('Impossible')
else:
  ans.sort()
  for i in ans:
    print(*i)