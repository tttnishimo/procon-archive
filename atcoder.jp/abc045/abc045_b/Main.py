a = []
a.append(list(input()))
a.append(list(input()))
a.append(list(input()))
x = a[0].pop(0)
while True:
  if x == 'a':
    if len(a[0]) == 0:
      print('A')
      break
    else:
      x = a[0].pop(0)
  elif x == 'b':
    if len(a[1]) == 0:
      print('B')
      break
    else:
      x = a[1].pop(0)
  elif x == 'c':
    if len(a[2]) == 0:
      print('C')
      break
    else:
      x = a[2].pop(0)