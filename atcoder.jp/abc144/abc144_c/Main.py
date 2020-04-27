n = int(input())
a = 1
res = pow(10,12)
for i in range(1,int(pow(n,1/2))+1):
  if n % i == 0:
    a = n // i
    res = min(res, a + i - 2)
print(res)