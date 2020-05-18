ans = 1
for i in range(1,int(input())+1):
  ans *= i
  ans %= 10**9+7
print(ans)