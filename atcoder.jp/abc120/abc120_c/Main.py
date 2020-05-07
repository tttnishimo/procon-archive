s = input()
a = [0,0]
res = 0
for i in range(len(s)):
  if s[i] == '0':
    a[0] += 1
  elif s[i] == '1':
    a[1] += 1
  if a[0] >= 1 and a[1] >= 1:
    res += 2
    a[0] -= 1
    a[1] -= 1
print(res)