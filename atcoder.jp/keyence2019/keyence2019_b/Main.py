s = input()
k = 'keyence'
flg_pre = 0
flg_post = 0
pre_match = 0
post_match = 0
if s[:6] == k or s[-7:] == k:
  print('YES')
else:
  for i in range(6):
    if s[i] == k[i] and flg_pre == 0:
      pre_match = i + 1
    else:
      flg_pre = 1
    if s[-i-1] == k[-i-1] and flg_post == 0:
      post_match = i + 1
    else:
      flg_post = 1
  if  pre_match + post_match >= 7:
    print('YES')
  else:
    print('NO')