N=int(input())
S=input()
ans=0
tmp=0
for i in range(N-1):
  if S[i]==S[i+1]:
    tmp+=1
  else:
    ans+=tmp*(tmp+1)//2
    tmp=0
ans+=tmp*(tmp+1)//2
print(ans)