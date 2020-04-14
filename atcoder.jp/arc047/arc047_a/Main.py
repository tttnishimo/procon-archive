a,b = map(int, input().split())
s = input()
tmp = 1
res = 0
for i in range(a):
  if s[i] == '+':
    tmp += 1
    if tmp > b:
      tmp = 1
      res += 1
  elif s[i] == '-':
    tmp -= 1
print(res)