n,k = map(int, input().split())
a = [0] * n
for i in range(k):
  d = int(input())
  b = list(map(int, input().split()))
  for j in range(len(b)):
    a[b[j]-1] = 1
res = 0
for i in range(n):
  if a[i] == 0:
    res += 1
print(res)