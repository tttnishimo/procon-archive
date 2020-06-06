n=int(input())
ans=0
flg1=0
flg2=0
for i in range(n):
  s=input()
  if s=='/':
    if flg2!=0:
      if flg1==flg2:
        ans+=1
      flg1=0
      flg2=0
    flg1+=1
  elif flg1!=0 and s=='\\':
    flg2+=1
if flg1==flg2:
  ans+=1
print(ans)