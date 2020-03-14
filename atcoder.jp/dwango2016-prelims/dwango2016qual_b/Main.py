n = int(input())
a = list(map(int, input().split()))
b = []
b.append(a[0])
for i in range(n-2):
  b.append(min(a[i], a[i + 1]))
b.append(a[-1])
print(*b)