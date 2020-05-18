import collections
n = int(input())
a = collections.Counter(list(input())).most_common()
if len(a) > 1:
  print(a[0][1],a[-1][1])
else:
  print(a[0][1],0)