n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = []
for i in range(m-1):
  b.append(a[i+1] - a[i])
b.sort(reverse=True)
del b[:n-1]
print(sum(b))