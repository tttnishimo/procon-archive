N=int(input())
ans=N*(N-1)//2
if N%2:
  ans-=1
print(ans)