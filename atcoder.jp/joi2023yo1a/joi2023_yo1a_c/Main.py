N=int(input())
S=input()
ans=0
b=0
for i in range(N):
  if S[i]=='L':
    b=max(b-1,0)
  else:
    b=min(b+1,2)
  if b==2:
    ans+=1
print(ans)