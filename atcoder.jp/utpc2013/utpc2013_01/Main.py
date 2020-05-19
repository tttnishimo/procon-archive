s=input()
flg=0
for i in range(len(s)):
  if i == 0 or i == 1:
    if s[i] in 'ADOPQRB':
      flg = 1
  elif i == 2:
    if s[i] not in 'ADOPQR':
      flg = 1
  else:
    if s[i] in 'ADOPQRB':
      flg = 1
if flg == 0:
  print('yes')
else:
  print('no')