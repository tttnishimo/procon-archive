n=int(input())
s=input()
tmp=0
ans=10**6
W=s.count('W')
for i in range(n):
  if s[i]=='W':
    ans=min(ans,n-1-(W-1)+tmp)
    tmp+=1
  else:
    ans=min(ans,n-1-W+tmp)
    tmp-=1
print(ans)