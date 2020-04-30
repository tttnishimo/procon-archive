s = input()
t = input()
arr = ['a', 't', 'c', 'o', 'd', 'e', 'r']
flg = 0
for i in range(len(s)):
  if s[i] == t[i]:
    pass
  elif s[i] == '@' and t[i] in arr:
    pass
  elif t[i] == '@' and s[i] in arr:
    pass
  else:
    flg = 1
if flg == 0:
  print('You can win')
else:
  print('You will lose')
