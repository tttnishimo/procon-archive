from collections import Counter
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(set(a))
if len(b) <= k:
  print(0)
else:
  c = sorted(Counter(a).values(), reverse=True)
  print(sum(c[k:]))