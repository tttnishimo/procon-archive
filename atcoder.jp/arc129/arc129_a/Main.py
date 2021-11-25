N,L,R=map(int,input().split())
ans=0
N=bin(N)[2:]
t=len(N)
for i in range(len(N)):
  if N[i]=='1':
    ans+=max(min(2**(t-i)-1,R)-max(2**(t-i-1),L)+1,0)
print(ans)