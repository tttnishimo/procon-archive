a,b = map(int, input().split())
n = 1
while a > b:
  a = a - b
  n = n + 1
print(n)