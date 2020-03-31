import collections
n,m = map(int, input().split())
a = collections.Counter(list(map(int, input().split()))).most_common()
if n == 1 or len(a) == 1:
  print(a[0][0])
else:
  if a[0][1] >= (n + 2) // 2 and a[1][1] < (n + 2) // 2:
    print(a[0][0])
  else:
    print('?')