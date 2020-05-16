n = int(input())
a = [[] for i in range(n)]
for i in range(n):
  s = input()
  for j in range(n):
    a[j].insert(0,s[j])
for i in range(n):
  print(*a[i],sep='')