a,b,c = map(int, input().split())
if a == b and b == c:
  print('No')
elif a == b and b != c:
  print('Yes')
elif a == c and b != c:
  print('Yes')
elif b == c and a != b:
  print('Yes')
else:
  print('No')