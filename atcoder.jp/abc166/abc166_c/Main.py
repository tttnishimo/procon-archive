n,m = map(int, input().split())
h = list(map(int, input().split()))
arr = [[] for i in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  arr[a-1].append(b-1)
  arr[b-1].append(a-1)
res = 0
for i in range(n):
  flg = 0
  for j in range(len(arr[i])):
    if h[i] <= h[arr[i][j]]:
      flg = 1
  if flg == 0:
    res += 1
print(res)