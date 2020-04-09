n,a,b = map(int, input().split())
if n == 1:
  if a != b:
    print(0)
  else:
    print(1)
elif n == 2:
  if a == b or a < b:
    print(1)
  else:
    print(0)
else:
  if  a > b:
    print(0)
  else:
    print((b - a) * (n - 2) + 1)