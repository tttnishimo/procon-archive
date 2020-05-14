n=int(input())
ans = 0
for i in range(n):
  a = list(map(int, input().split()))
  ans = max(ans,sum(a)-a[4]*79/90)
print(ans)