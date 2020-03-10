import math
n = int(input())
tmp = []
for i in range(1,44722):
  if i*(i+1)/2 >= n:
    tmp.append(i)
print(tmp[0])