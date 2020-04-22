s = input()
flg = 0
for i in range(len(s)):
  if i % 2 == 0 and s[i] == 'L':
    flg = 1
  if i % 2 == 1 and s[i] == 'R':
    flg = 1
if flg == 0:
  print('Yes')
else:
  print('No')
