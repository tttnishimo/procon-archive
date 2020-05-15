import collections
n = int(input())
ind = collections.Counter('indeednow')
for i in range(n):
  s = input()
  if collections.Counter(s) == ind:
    print('YES')
  else:
    print('NO')