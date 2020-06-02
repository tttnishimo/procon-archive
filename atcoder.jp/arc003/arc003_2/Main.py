n = int(input())
a = []
for i in  range(n):
  a.append(''.join(list(reversed(input()))))
a.sort()
for i in  range(n):
  print(''.join(list(reversed(a[i]))))