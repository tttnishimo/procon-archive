s = input()
res = 999
for i in range(len(s)-2):
  res = min(res, abs(int(s[i:i+3]) - 753))
print(res)