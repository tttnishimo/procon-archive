n,m = map(int, input().split())
s = input()
num = '0123456789'
flg = 0
for i in range(len(s)):
  if i < n-1:
    if s[i] not in num:
      flg = 1
  elif i == n:
    if s[i] != '-':
      flg = 1
  else:
    if s[i] not in num:
      flg = 1
if flg == 0:
  print('Yes')
else:
  print('No')
