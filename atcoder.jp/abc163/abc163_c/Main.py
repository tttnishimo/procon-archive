n = int(input())
a = list(map(int, input().split()))
res = [0]*n
for i in range(n-1):
  res[a[i]-1] += 1
print(*res)