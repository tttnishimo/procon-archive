s=input()
n=len(s)
ans=n
flg=0
for i in range(n):
  if s[i]=='S':
    flg+=1
  elif flg>0 and s[i]=='T':
    flg-=1
    ans-=2
  else:
    flg=0
print(ans)