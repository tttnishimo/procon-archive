a,b,c = map(int, input().split())
if (c > a and b > c) or (c < a and b < c):
  print('Yes')
else:
  print('No')
