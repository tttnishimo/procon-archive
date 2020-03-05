import math
a = int(input())
arr = []
maxlen = 0
for i in range(a):
  arr.append(list(map(int, input().split())))
for i in range(a):
  for j in range(i + 1, a):
    len = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2
    if maxlen < len:
      maxlen = len
print(math.sqrt(maxlen))