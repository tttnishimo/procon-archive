s = input().lower()
flg = 0
for i in range(len(s)):
  if s[i] == 'i' and flg == 0:
    flg = 1
  elif s[i] == 'c' and flg == 1:
    flg = 2
  elif s[i] == 't' and flg == 2:
    flg = 3
if flg == 3:
  print('YES')
else:
  print('NO')