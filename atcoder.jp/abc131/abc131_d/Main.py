n = int(input())
arr = []
tmp = 0
flg = 0
for i in range(n):
  a,b = map(int, input().split())
  arr.append([b,a])
arr.sort()
for i in range(n):
  tmp += arr[i][1]
  if tmp > arr[i][0]:
    flg = 1
if flg == 0:
  print('Yes')
else:
  print('No')