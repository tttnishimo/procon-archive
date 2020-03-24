n = int(input())
s = input()
flg = 0
res = 1
for i in range(n-1):
  if flg == 0 and s[i] == s[i+1]:
    flg = 1
  elif flg == 1 and s[i] == s[i+1]:
    pass
  else:
    flg = 0
    res += 1
print(res)