n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
lower = b[int(n/2) - 1]
upper = b[int(n/2)]
for i in range(n):
  if a[i] <= lower:
    print(upper)
  else:
    print(lower)