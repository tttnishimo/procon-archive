a,b,c,d = map(int, input().split())
i = 0
while a > 0 and c > 0:
  if i % 2 == 0:
    c -= b
    i += 1
  else:
    a -= d
    i += 1
if a <= 0:
  print('No')
else:
  print('Yes')