for i in range(5):
  if i == 0:
    a = int(input())
  elif i == 1 or i == 2 or i == 3:
    tmp = int(input())
  else:
    b = int(input())
k = int(input())
if k >= b - a:
  print("Yay!")
else:
  print(":(")