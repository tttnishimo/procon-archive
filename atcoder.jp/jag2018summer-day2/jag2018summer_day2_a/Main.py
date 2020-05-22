x,y,z=map(int,input().split())
i=0
while True:
  n = i*(10**9+7) + z
  if n % 107 == y and n % 17 == x:
    break
  i += 1
print(n)