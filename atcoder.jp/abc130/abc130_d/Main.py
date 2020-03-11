from itertools import accumulate
n,k = map(int, input().split())
a = list(map(int, input().split()))
a = list(accumulate(a))
a.insert(0, 0)
ans = 0
l = 0
r = 0
while r < n + 1:
  if a[r] - a[l] >= k:
    ans += n - r + 1
    l += 1
  else:
    r += 1
print(ans)