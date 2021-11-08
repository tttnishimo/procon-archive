S=input()
a=0
b=0
flg=0
for i in S:
  if i=='*':
    flg=1
  elif flg==0:
    if i=='(':
      a+=1
    else:
      a-=1
  else:
    if i==')':
      b+=1
    else:
      b-=1
print(min(a,b))