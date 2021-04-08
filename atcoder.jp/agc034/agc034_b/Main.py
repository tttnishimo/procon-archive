s=input().replace('BC','D')
ans=0
tmp=0
for i in range(len(s)):
  if s[i]=='A':
    tmp+=1
  elif s[i]=='D':
    ans+=tmp
  else:
    tmp=0
print(ans)