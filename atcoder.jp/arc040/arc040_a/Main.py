n = int(input())
red = 0
blue = 0
for i in range(n):
  s = input()
  red += s.count('R')
  blue += s.count('B')
if red > blue:
  print('TAKAHASHI')
elif blue > red:
  print('AOKI')
else:
  print('DRAW')