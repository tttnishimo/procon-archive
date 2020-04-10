n,m = map(int, input().split())
a = [0,n]
for i in range(m):
  s,t = map(int, input().split())
  a[0] = max(a[0], s)
  a[1] = min(a[1], t)
print(max(a[1] - a[0] + 1, 0))