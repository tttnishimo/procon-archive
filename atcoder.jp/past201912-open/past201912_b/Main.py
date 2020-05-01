n = int(input())
a = int(input())
for i in range(n-1):
  b = int(input())
  if b > a:
    print('up', b - a)
  elif b == a:
    print('stay')
  else:
    print('down', a - b)
  a = b
  