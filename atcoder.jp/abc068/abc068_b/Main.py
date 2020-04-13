n = int(input())
for i in range(8):
  if 2 ** i <= n:
    res = 2 ** i
print(res)