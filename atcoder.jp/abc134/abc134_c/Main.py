n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
max_1 = max(a)
a[a.index(max_1)] = -1
max_2 = max(a)
a[a.index(-1)] = max_1
for i in range(0,n):
  if a[i] == max_1:
    print(max_2)
  else:
    print(max_1)