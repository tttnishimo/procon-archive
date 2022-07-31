N=int(input())
ans=10**15
for i in range(1,int(N**.5)+1):
  if N%i==0:
    ans=min(ans,(i+N//i)*2)
print(ans)