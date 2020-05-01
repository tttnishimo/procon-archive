s = input()
al = 'abcdefghijklmnopqrstuvwxyz'
flg = 0
if s[0] in al:
  flg = 1
elif s[1] in al:
  flg = 1
elif s[2] in al:
  flg = 1
if flg == 0:
  if s[0] == '0':
    s = s[1:]
    if s[0] == '0':
      s = s[1:]
  print(2 * int(s))
else:
  print('error')