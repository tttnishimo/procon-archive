n = int(input())
a = list(map(int, input().split()))
c_4 = 0
c_2 = 0
for i in range(n):
  if a[i] % 4 == 0:
    c_4 += 1
  elif a[i] % 2 == 0:
    c_2 += 1
if c_4 >= n // 2:
  print('Yes')
elif c_4 * 2 + c_2 >= n:
  print('Yes')
else:
  print('No')