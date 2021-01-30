a=list(map(str,input().split()))
ans=[]
tmp=[]
for i in range(len(a)):
  if a[i]=='not':
    tmp.append(a[i])
  else:
    if len(tmp)>=2:
      tmp=['not']*(len(tmp)%2)
    ans+=tmp
    ans.append(a[i])
    tmp=[]
ans+=tmp
print(*ans)