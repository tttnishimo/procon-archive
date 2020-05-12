a = {}
for i in range(int(input())):
  b,c = map(int, input().split())
  if b > c:
    b,c = c,b
  b = str(str(b)+'-'+str(c))
  a[b] = 1
print(len(a))
