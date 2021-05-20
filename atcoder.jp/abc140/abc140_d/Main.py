N,K=map(int,input().split())
S=input()
a=[]
t=0
for i in range(1,N):
  if S[i]==S[i-1]:
    t+=1
  else:
    a.append(t)
    t=0
a.append(t)
ans=sum(a)
if K<=(len(a)-1)//2:
  ans+=2*K
else:
  ans+=len(a)-1
print(ans)