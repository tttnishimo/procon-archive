n = int(input())
if n < 100:
  print("00")
elif n >= 100 and n < 1000:
  print("0{}".format(n//100))
elif n >=1000 and n <= 5000:
  print(n//100)
elif n >= 6000 and n <= 30000:
  print(n//1000 + 50)
elif n >= 35000 and n <= 70000:
  print((n//1000 - 30) // 5 + 80)
else:
  print("89")