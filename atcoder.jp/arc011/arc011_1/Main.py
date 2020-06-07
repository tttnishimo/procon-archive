m,n,N=map(int,input().split())
ans=N
remain=N%m
recycle=N//m*n
while recycle+remain>=m:
  ans+=recycle
  recycle,remain=(recycle+remain)//m*n,(recycle+remain)%m
ans+=recycle
print(ans)