s = input()
t = input()
flg = 0
for i in range(len(s)):
  if s == t:
    flg = 1
  s = s[1:] + s[0]
if flg == 1:
  print('Yes')
else:
  print('No')