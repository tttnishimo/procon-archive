N=int(input())
S=input()
f=0
a=set()
for i in range(N):
  if S[i]=='"' and f==0:
    f=1
  elif S[i]=='"' and f==1:
    f=0
  if S[i]==',' and f==0:
    a.add(i)
ans=''
for i in range(N):
  if i in a:
    ans+='.'
  else:
    ans+=S[i]
print(ans)