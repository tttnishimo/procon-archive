n = int(input())
a = []
flag = 0
d = 0
for i in range(n):
  a.append(int(input()))
a.sort()
for i in range(n - 1):
  if flag == 1:
    flag = 0
  elif a[i] == a[i + 1]:
    d = d + 2
    flag = 1
print(len(a) - d)