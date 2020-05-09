import collections
n = int(input())
a = list(map(int, input().split()))

c_0 = collections.Counter(a[::2])
c_1 = collections.Counter(a[1::2])

if len(c_0.most_common()) == 1 and len(c_1.most_common()) == 1:
  if c_0.most_common()[0][0] == c_1.most_common()[0][0]:
    print(n // 2)
  else:
    print(0)
elif len(c_0.most_common()) == 1:
  if c_0.most_common()[0][0] == c_1.most_common()[0][0]:
    print(n // 2 - c_1.most_common()[1][1])
  else:
    print(n // 2 - c_1.most_common()[0][1])
elif len(c_1.most_common()) == 1:
  if c_0.most_common()[0][0] == c_1.most_common()[0][0]:
    print(n // 2 - c_0.most_common()[1][1])
  else:
    print(n // 2 - c_0.most_common()[0][1])
elif c_0.most_common()[0][0] == c_1.most_common()[0][0]:
  if c_0.most_common()[0][1] > c_1.most_common()[0][1]:
    print(n - c_0.most_common()[0][1] - c_1.most_common()[1][1])
  elif c_0.most_common()[0][1] < c_1.most_common()[0][1]:
    print(n - c_0.most_common()[1][1] - c_1.most_common()[0][1])
  else:
    print(n - c_0.most_common()[0][1] - max(c_0.most_common()[1][1],c_1.most_common()[1][1]))
else:
  print(n - c_0.most_common()[0][1] - c_1.most_common()[0][1])