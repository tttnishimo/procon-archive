n = int(input())
a = list(map(int, input().split()))
res = 0
for i, val in enumerate(a):
  if a[val - 1] == i + 1:
    res += 1
print(res//2)