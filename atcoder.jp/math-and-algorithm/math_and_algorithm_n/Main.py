N=int(input())
ans=[]
for i in range(2,int(N**.5)+1):
  while N%i==0:
    ans.append(i)
    N//=i
if N!=1:
  ans.append(N)
print(*ans)