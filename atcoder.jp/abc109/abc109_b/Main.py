n = int(input())
flg = 0
arr = []*n
arr.append(input())
for i in range(n-1):
  tmp = input()
  if arr[-1][-1] != tmp[0]:
    flg = 1
  if tmp in arr:
    flg = 1
  arr.append(tmp)
if flg == 0:
  print('Yes')
else:
  print('No')