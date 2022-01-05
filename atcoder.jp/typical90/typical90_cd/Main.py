L,R=map(int,input().split())
ans=0
for i in range(len(str(L)),len(str(R))+1):
  U=min(R,10**i-1)
  D=max(L,10**(i-1))
  ans+=i*(U*(U+1)//2-(D-1)*D//2)
  ans%=1000000007
print(ans)