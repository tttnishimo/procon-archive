n = int(input())
arr = []
tmp = 0
res = -1
for i in range(n):
  arr.append(int(input()))
for i in range(n):
  if arr[tmp] == 2 and res == -1:
    res = i + 1
  tmp = arr[tmp] - 1
print(res)