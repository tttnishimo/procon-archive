n = int(input())
if n % 40 == 0:
  print(1)
elif n % 20 == 0:
  print(20)
elif n // 20 % 2 == 1:
  print(21 - (n % 20))
else:
  print(n%20)