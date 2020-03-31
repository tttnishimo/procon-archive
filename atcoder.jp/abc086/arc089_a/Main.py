n = int(input())
arr = [[0,0,0]]
flg = 0
for i in range(n):
  arr.append(list(map(int, input().split())))
  if arr[i+1][0]-arr[i][0] < arr[i+1][1] + arr[i+1][2] - arr[i][1] - arr[i][2] or (arr[i+1][0]-arr[i][0]) % 2 != (arr[i+1][1] + arr[i+1][2] - arr[i][1] - arr[i][2]) % 2:
    flg = 1
if flg == 0:
  print('Yes')
else:
  print('No')