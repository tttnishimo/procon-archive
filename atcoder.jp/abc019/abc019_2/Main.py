s = input()
res = ''
flg = 0
for i in range(len(s)):
  if len(res) == 0:
    res += s[i]
    flg += 1
  elif s[i] == s[i-1]:
    flg += 1
  else:
    res += str(flg)
    res += s[i]
    flg = 1
res += str(flg)
print(res)