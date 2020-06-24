n=int(input())
a=[input()]
b=[]
flg=0
for i in range(1,n):
  tmp=input()
  if i%2==0:
    if a.count(tmp)>=1 or b.count(tmp)>=1 or tmp[0] != b[-1][-1]:
      flg=1
      break
    else:
      a.append(tmp)
  else:
    if a.count(tmp)>=1 or b.count(tmp)>=1 or tmp[0] != a[-1][-1]:
      flg=2
      break
    else:
      b.append(tmp)
if flg==1:
  print('LOSE')
elif flg==2:
  print('WIN')
else:
  print('DRAW')