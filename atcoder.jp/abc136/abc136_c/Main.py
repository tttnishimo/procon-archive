n = int(input())
a = list(map(int, input().split()))
flg = 0
a[0] -= 1
for i in range(1,n):
  if a[i] >= a[i-1] + 1:
    a[i] -= 1
  elif a[i] < a[i-1]:
    flg = 1
if flg == 1:
  print('No')
else:
  print('Yes')