s = input()
flg = 0
for i in range(len(s)):
  if s.count(s[i]) >= 2:
    flg = 1
if flg == 0:
  print('yes')
else:
  print('no')