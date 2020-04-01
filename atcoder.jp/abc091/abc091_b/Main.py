import collections
n = int(input())
arr = []
for i in range(n):
  arr.append(input())
m = int(input())
for i in range(m):
  s = input()
  if s in arr:
    arr.remove(s)
if len(arr) == 0:
  print(0)
else:
  arr = collections.Counter(arr)
  print(arr.most_common()[0][1])