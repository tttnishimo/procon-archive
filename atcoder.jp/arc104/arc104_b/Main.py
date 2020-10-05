n,s=map(str,input().split())
n=int(n)
ans=0
for i in range(n):
  a,c=0,0
  for j in range(i,n):
    if s[j]=='A':
      a+=1
    elif s[j]=='T':
      a-=1
    elif s[j]=='C':
      c+=1
    else:
      c-=1
    if a==0 and c==0:
      ans+=1
print(ans)