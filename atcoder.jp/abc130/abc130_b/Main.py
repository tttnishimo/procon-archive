a,b = map(int, input().split())
arr = list(map(int, input().split()))
tmp = 0
res = 1
for i in range(a):
  tmp += arr[i]
  if tmp <= b:
    res += 1
print(res)