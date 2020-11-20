a=[input() for _ in range(10)]
flg=0
for i in range(10):
  tmp=0
  for j in range(10):
    if a[j][i]=='o':
      tmp=1
  if tmp==0:
    flg=1
if flg==1:
  print('No')
else:
  print('Yes')