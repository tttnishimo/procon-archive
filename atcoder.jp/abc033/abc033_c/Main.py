s=input()
ans=0
flg=0
for i in range(1,len(s)):
  if s[i]=='+':
    if s[flg:i].count('0')==0:
      ans+=1
    flg=i
if s[flg:].count('0')==0:
  ans+=1
print(ans)