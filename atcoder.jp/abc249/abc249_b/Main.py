S=input()
big='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
f_b=0
f_s=0
for s in S:
  if S.count(s)>1:
    print('No')
    exit()
  if s in big:
    f_b=1
  else:
    f_s=1
if f_b and f_s:
  print('Yes')
else:
  print('No')