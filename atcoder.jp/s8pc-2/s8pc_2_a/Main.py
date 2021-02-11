s=input()
flg=0
ans=0
for i in range(len(s)):
  if flg==0 and s[i]=='I':
    flg=1
    ans+=1
  if flg==1 and s[i]=='O':
    flg=0
    ans+=1
if flg==0:
  ans=max(ans-1,0)
print(ans)