n,m=map(int,input().split())
for i in range(m%2,n+1,2):
  if (n-i)*2<=m-3*i<=(n-i)*4:
    b=i
    c=(m-3*i)//2-n+i
    a=n-b-c
    print(a,b,c)
    exit()
print(-1,-1,-1)