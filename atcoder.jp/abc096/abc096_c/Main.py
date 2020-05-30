h,w=map(int,input().split())
a=['.'*(w+2)]
for i in range(h):
  a.append('.'+input()+'.')
a.extend(['.'*(w+2)])
flg=0
for i in range(1,h+1):
  for j in range(1,w+1):
    if a[i][j] == '#':
      if a[i-1][j] == '.' and a[i][j-1] == '.' and a[i+1][j] == '.' and a[i][j+1] == '.':
        flg = 1
if flg == 0:
  print('Yes')
else:
  print('No')