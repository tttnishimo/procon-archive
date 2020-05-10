s = input()
t = input()
flg = 0
for i in range(len(s)):
  if s[i] != t[i]:
    flg = 1
if flg == 0:
  print('Yes')
else:
  print('No')