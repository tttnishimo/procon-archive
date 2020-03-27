s = input()
tmp = 'CODEFESTIVAL2016'
res = 0
for i in range(16):
  if s[i] != tmp[i]:
    res += 1
print(res)