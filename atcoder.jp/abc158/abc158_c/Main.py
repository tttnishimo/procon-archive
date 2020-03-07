tax = []
a,b = map(int, input().split())
for i in range(1,10000):
  tax8 = int(i * 0.08)
  if tax8 == a:
    if int(i * 0.1) == b:
      tax.append(i)
if tax == []:
  print(-1)
else:
  print(tax[0])