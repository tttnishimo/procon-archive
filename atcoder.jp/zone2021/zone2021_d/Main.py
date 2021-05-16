S=input()
ans=''
flg=False
for i in S:
  if i=='R':
    flg=not flg
  else:
    if not flg:
      ans+=i
    else:
      ans=i+ans
  if len(ans)>1:
    if ans[-1]==ans[-2]:
      ans=ans[:-2]
    elif ans[0]==ans[1]:
      ans=ans[2:]
if not flg:
  print(ans)
else:
  print(''.join(list(reversed(ans))))