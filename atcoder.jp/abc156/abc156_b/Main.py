a, b = map(int, input().split())
num = 1
while a >= b:
  a = a / b
  num = num + 1
print(num)