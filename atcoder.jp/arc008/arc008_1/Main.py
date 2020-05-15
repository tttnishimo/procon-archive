n = int(input())
ans = 0
ans += n // 10 * 100
if n % 10 <= 6:
  ans += n % 10 * 15
else:
  ans += 100
print(ans)
