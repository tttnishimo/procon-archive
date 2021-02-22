n=int(input())
s=input()
init_a=-1
flg=0
ans=0
for i in range(len(s)):
  if s[i]=='A':
    flg+=1
  else:
    ans+=flg*(flg+1)//2
    if init_a==-1:
      init_a=flg
    flg=0
ans+=flg*(flg+1)//2
if init_a==-1:
  init_a=len(s)
if n==1:
  print(ans)
elif len(s)==init_a:
  print((len(s)*n)*(len(s)*n+1)//2)
else:
  last_a=0
  for i in range(len(s)):
    if s[-1-i]=='A':
      last_a+=1
    else:
      break
  i=init_a*(init_a+1)//2
  l=last_a*(last_a+1)//2
  print((ans-i-l)*n+(init_a+last_a)*(init_a+last_a+1)//2*(n-1)+i+l)