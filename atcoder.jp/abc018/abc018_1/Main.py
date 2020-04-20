a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
  print(1)
elif a < b and a < c:
  print(3)
else:
  print(2)
if b > a and b > c:
  print(1)
elif b < a and b < c:
  print(3)
else:
  print(2)
if c > b and c > a:
  print(1)
elif c < b and c < a:
  print(3)
else:
  print(2)
