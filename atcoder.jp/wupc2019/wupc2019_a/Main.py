s = input()
flg = -1
for i in range(len(s)):
  if s[i] == 'W' and flg == -1:
#    s = s[:i] + 'A' + s[i+1:]
    flg = i
  elif s[i] == 'W' and flg != -1:
    pass
  elif s[i] == 'A' and flg != -1:
    s = s[:flg] + 'A' + 'C' * (i - flg) + s[i+1:]
    flg = -1
  elif flg != -1:
    flg = -1
print(s)