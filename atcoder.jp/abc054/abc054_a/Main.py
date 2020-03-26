a,b = map(int, input().split())
if a != 1 and b != 1:
  if a > b:
    print('Alice')
  elif a == b:
    print('Draw')
  else:
    print('Bob')
elif a == 1 and b == 1:
  print('Draw')
elif a == 1:
  print('Alice')
else:
  print('Bob')