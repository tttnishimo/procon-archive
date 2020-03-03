n = 10 ** 9
k = 2 * 10 ** 5
mod = 10**9 + 7

modinv_table = [-1] * (k+1)
modinv_table[1] = 1
for i in range(2, k+1):
  modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def binomial_coefficients(n, k):
  ans = 1
  for i in range(k):
    ans *= n-i
    ans *= modinv_table[i + 1]
    ans %= mod
  return ans

s,a,b = map(int, input().split())
sum = 0
if s == 2:
  pass
else:
  d = pow(2, s, mod) - 1
  sum = d - binomial_coefficients(s, a) - binomial_coefficients(s, b)
while sum < 0:
  sum = sum + mod
print(sum)