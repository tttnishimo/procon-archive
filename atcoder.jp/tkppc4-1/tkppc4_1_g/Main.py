q=int(input())
n=list(map(int,input().split()))
for i in range(q):
  if n[i]==0 or n[i]==1:
    pass
  elif n[i]%3==0:
    n[i]=pow(3,n[i]//3,1000000007)
  elif n[i]%3==1:
    n[i]=pow(3,n[i]//3-1,1000000007)*4%1000000007
  else:
    n[i]=pow(3,n[i]//3-1,1000000007)*6%1000000007
print(*n)