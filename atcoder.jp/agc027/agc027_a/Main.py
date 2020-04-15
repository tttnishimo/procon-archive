a,b = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = 0
tmp = 0
for i in range(a):
  tmp += arr[i]
  if tmp <= b:
    res = i+1
if res == a and tmp < b:
  res -= 1
print(res)