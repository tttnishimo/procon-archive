s=input()
suit='SHDC'
a={'S':0,'H':0,'D':0,'C':0}
ans=s
for i in range(len(s)):
  if s[i] in suit:
    t=s[i]
    n=''
  else:
    n+=s[i]
  if n=='10' or n=='J' or n=='Q' or n=='K' or n=='A':
    a[t]+=1
    if max(a.values())==5:
      break
ans=ans[:i+1].replace(t+'10','')
ans=ans.replace(t+'J','')
ans=ans.replace(t+'Q','')
ans=ans.replace(t+'K','')
ans=ans.replace(t+'A','')
if ans=='':
  print(0)
else:
  print(ans)