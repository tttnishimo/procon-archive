n,p=map(int,input().split())
ans=1
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append([b, e])
        b, e = b + 1, 0
    if n > 1:
        fct.append([n, 1])
    return fct
p=factorize(p)
for i in p:
  while i[1]>=n:
    i[1]-=n
    ans*=i[0]
print(ans)