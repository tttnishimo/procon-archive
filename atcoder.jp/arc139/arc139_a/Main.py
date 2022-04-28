N=int(input())
T=list(map(int,input().split()))
ans=0
for i in T:
  if ans<2**i:
    ans=2**i
  else:
    for j in range(i):
      if bin(ans)[-j-1]=='1':
        ans-=2**j
    ans+=2**i
    if bin(ans)[-i-1]=='0':
      ans+=2**i
print(ans)