s = input()
ans = 0
tmp = 0
flg = 0
for i in range(len(s)):
  if s[i] == 'A' and flg == 0:
    ans += 1
    flg = 1
  elif flg == 1 and s[i] == 'Z':
    flg = 2
    ans += 1
  elif flg == 1:
    ans += 1
  elif flg == 2 and s[i] == 'Z':
    ans += tmp+1
    tmp = 0
  elif flg == 2:
    tmp += 1
print(ans)