n = int(input())
arr = [0]*n
for i in range(n):
  m = int(input())
  arr[m-1] += 1
if 0 not in arr:
  print('Correct')
else:
  print(arr.index(2)+1, arr.index(0)+1)