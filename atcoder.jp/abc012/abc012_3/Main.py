n = 2025 - int(input())
i = 1
while i <= n:
  if n % i == 0 and i < 10 and n//i < 10:
    print(str(i) + ' x ' + str(n // i))
  i += 1