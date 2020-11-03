n=int(input())
a=list(map(int,input().split()))
b=[a[n-i-1]-n+i for i in range(n)]
ans=[]
while 0 in b:
  m=b.index(0)
  ans.insert(0,len(b)-m)
  b=[b[i]+1 for i in range(m)]+b[m+1:]
if len(ans)==n:
  print(*ans,sep='\n')
else:
  print(-1)