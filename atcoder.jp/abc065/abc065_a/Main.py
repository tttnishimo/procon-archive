a,b,c = map(int, input().split())
if b >= c:
  print('delicious')
elif c - b <= a:
  print('safe')
else:
  print('dangerous')
