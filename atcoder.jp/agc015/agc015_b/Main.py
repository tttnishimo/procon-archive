s = input()
res = 0
n = len(s)
for i in range(n):
  if s[i] == "U":
    res += n - i - 1 + 2 * i
  else:
    res += 2 * (n - i - 1) + i
print(res)