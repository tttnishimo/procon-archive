s=input()
ans=0
flg=0
if len(s)<=1:
  print(0)
else:
  if s[:2]=='25':
    flg=1
    ans=1
  for i in range(1,len(s)-1):
    if flg>=1:
      if s[i:i+2]=='25':
        flg+=1
        ans+=flg
      elif s[i:i+2]=='52':
        pass
      else:
        flg=0
    elif s[i:i+2]=='25':
      flg+=1
      ans+=1
  print(ans)