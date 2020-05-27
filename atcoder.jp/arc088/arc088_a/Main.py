n,m=map(int,input().split())
ans = 1
while m >= n*2**ans:
  ans +=1
print(ans)