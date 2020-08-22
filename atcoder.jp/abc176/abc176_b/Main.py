s=input()
ans=0
for i in range(len(s)):
  ans+=int(s[i])
if ans%9==0:
  print('Yes')
else:
  print('No')