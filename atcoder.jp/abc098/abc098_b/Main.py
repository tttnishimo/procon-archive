n = int(input())
s = input()
a = [0]*26
al = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
  a[al.index(s[i])] += 1
b = [0]*26
res = 0
for i in range(n):
  b[al.index(s[i])] += 1
  tmp = 0
  for j in range(26):
    if b[j] >= 1 and a[j] - b[j] >= 1:
      tmp += 1
  res = max(res, tmp)
print(res)