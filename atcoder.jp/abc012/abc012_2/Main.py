n = int(input())
a = str(n // 3600)
if int(a) < 10:
  a = '0' + a
b = str(n % 3600 // 60)
if int(b) < 10:
  b = '0' + b
c = str(n % 60)
if int(c) < 10:
  c = '0' + c
print(a + ':' + b + ':' + c)