n = int(input())
a = list(map(int, input().split()))
res = a[-1]
for i in range(n-1):
  if a[i+1] < a[i]:
    res += a[i] - a[i+1]
print(res)