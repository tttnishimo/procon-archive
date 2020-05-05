a,b,c = map(int, input().split())
d = b-a
while True:
  if b >= c:
    break
  b += d
print(b)