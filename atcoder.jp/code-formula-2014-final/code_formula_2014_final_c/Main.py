s=input()
ans=[]
flg=-1
for i in range(len(s)):
  if flg==-1 and s[i]=='@':
    flg=i
  elif flg>=0 and s[i]=='@' and s[i-1]=='@':
    flg=i
  elif flg>=0 and s[i]==' ':
    if s[flg+1:i]!='' and (s[flg+1:i] not in ans):
      ans.append(s[flg+1:i])
    flg=-1
  elif flg>=0 and s[i]=='@':
    if s[flg+1:i]!='' and (s[flg+1:i] not in ans):
      ans.append(s[flg+1:i])
    flg=i
if flg>=0:
  if s[flg+1:]!='' and (s[flg+1:] not in ans):
    ans.append(s[flg+1:])
ans.sort()
print(*ans,sep='\n')