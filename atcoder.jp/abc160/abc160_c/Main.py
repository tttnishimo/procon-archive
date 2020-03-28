k,n = map(int, input().split())
a = list(map(int, input().split()))
tmp = [a[0] + k - a[-1]]
for i in range(n-1):
  tmp.append(a[i + 1] - a[i])
print(k - max(tmp))