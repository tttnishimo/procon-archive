n,m = map(int, input().split())
arr = []
res = 0
count = 0
for i in range(n):
  arr.append(list(map(int, input().split())))
arr = sorted(arr)
i = 0
while count < m:
  count += arr[i][1]
  if count < m:
    res += arr[i][0] * arr[i][1]
  else:
    res += (arr[i][1] - count + m) * arr[i][0]
  i += 1
print(res)