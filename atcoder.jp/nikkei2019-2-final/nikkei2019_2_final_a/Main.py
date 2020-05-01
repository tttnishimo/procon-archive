n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
  left = 0
  right = 0
  for j in range(n):
    if a[j] < a[i] and j < i:
      left += 1
    elif a[j] < a[i] and j > i:
      right += 1
  res += left * right
print(res)
