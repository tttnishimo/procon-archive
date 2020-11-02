import collections
n=input()
if len(n)==1:
  if n=='8':
    print('Yes')
  else:
    print('No')
elif len(n)==2:
  if n=='16' or n=='61' or n=='24' or n=='42' or n=='32' or n=='23' or n=='48' or n=='84' or n=='56' or n=='65' or n=='46' or n=='64' or n=='72' or n=='27' or n=='88' or n=='96' or n=='69':
    print('Yes')
  else:
    print('No')
else:
  nl=collections.Counter(n)
  ans='No'
  for i in range(13,125):
    m=str(8*i)
    ml=collections.Counter(m)
    flg=0
    for j in ml:
      if nl[j]<ml[j]:
        flg=1
    if flg==0:
      ans='Yes'
  print(ans)