import numpy as np
n,m,c = map(int, input().split())
b = np.array(list(map(int, input().split())))
res = 0
for i in range(n):
  a = np.array(list(map(int, input().split())))
  if sum(a * b) + c > 0:
    res += 1
print(res)
