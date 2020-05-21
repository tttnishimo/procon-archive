x,k=map(int,input().split())
if x > 10**k:
  ans = x // 10**k * 10**k
else:
  ans = 10**k
while True:
  if ans > x and ans % 10**k == 0:
    break
  ans += 10**k
print(ans)