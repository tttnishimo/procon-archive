a,b,c = map(int, input().split())
d,e,f = map(int, input().split())
g,h,i = map(int, input().split())
aa = 0
bb = 0
cc = 0
dd = 0
ee = 0
ff = 0
gg = 0
hh = 0
ii = 0

j = int(input())

for k in range(j):
  l = int(input())
  if a == l:
    aa = 1
  elif b == l:
    bb = 1
  elif c == l:
    cc = 1
  elif d == l:
    dd = 1
  elif e == l:
    ee = 1
  elif f == l:
    ff = 1
  elif g == l:
    gg = 1
  elif h == l:
    hh = 1
  elif i == l:
    ii = 1
if aa == 1 and bb == 1 and cc == 1:
  print('Yes')
elif dd == 1 and ee == 1 and ff == 1:
  print('Yes')
elif gg == 1 and hh == 1 and ii == 1:
  print('Yes')
elif aa == 1 and dd == 1 and gg == 1:
  print('Yes')
elif bb == 1 and ee == 1 and hh == 1:
  print('Yes')
elif cc == 1 and ff == 1 and ii == 1:
  print('Yes')
elif aa == 1 and ee == 1 and ii == 1:
  print('Yes')
elif cc == 1 and ee == 1 and gg == 1:
  print('Yes')
else:
  print('No')