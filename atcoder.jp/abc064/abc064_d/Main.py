n=int(input())
s=input()
tmp=''
ans=''
flg=0
for i in range(n):
  tmp+=s[i]
  if s[i]=='(':
    flg+=1
  else:
    if flg>0:
      flg-=1
    else:
      tmp='('+tmp
flg=0
for i in range(len(tmp)):
  ans=tmp[-i-1]+ans
  if tmp[-i-1]==')':
    flg+=1
  else:
    if flg>0:
      flg-=1
    else:
      ans=ans+')'
print(ans)