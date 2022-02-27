N=int(input())
S=input()
ans=N*(N-1)//2
t=0
for i in range(1,N):
  if S[i]==S[i-1]:
    t+=1
    ans-=t
  else:
    t=0
print(ans)