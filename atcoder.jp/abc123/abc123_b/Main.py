res = 0
frac = 10
for i in range(5):
  a = int(input())
  if a % 10 != 0:
    frac = min(frac, a % 10)
  res += -(-a // 10) *10
print(res + frac - 10)