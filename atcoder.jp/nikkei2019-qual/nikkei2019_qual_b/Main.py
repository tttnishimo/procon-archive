n = int(input())
a = input()
b = input()
c = input()
res = 0
for i in range(n):
  if a[i] == b[i] and b[i] == c[i]:
    pass
  elif a[i] != b[i] and b[i] != c[i] and c[i] != a[i]:
    res += 2
  else:
    res += 1
print(res)