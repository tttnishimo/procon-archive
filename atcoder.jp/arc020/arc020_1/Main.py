a,b = map(int, input().split())
a = abs(a)
b = abs(b)
if a < b:
  print('Ant')
elif a == b:
  print('Draw')
else:
  print('Bug')