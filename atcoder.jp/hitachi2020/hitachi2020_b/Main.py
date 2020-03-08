a,b,m = map(int, input().split())
pricea = list(map(int, input().split()))
priceb = list(map(int, input().split()))
min = min(pricea) + min(priceb)
for i in range(m):
  x, y, c = map(int, input().split())
  tmp = pricea[x - 1] + priceb[y - 1] - c
  if tmp < min:
    min = tmp
print(min)