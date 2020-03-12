l,r = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for i in range(len(a)):
  if b.count(a[i]) >= 1:
    ans = ans + 1
    b.remove(a[i])
print(ans)