n,x,y = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
x += sum(a[::2])
y += sum(a[1::2])
if x > y:
  print('Takahashi')
elif x == y:
  print('Draw')
else:
  print('Aoki')