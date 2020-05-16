n,m=map(int,input().split())
a = [0]*n
seen = [0]*n
flg = 0
ans = 0
for i in range(m):
  tmp = list(map(int,input().split()))
  if seen[tmp[0]-1] == 0:
    a[tmp[0]-1] = tmp[1]
    seen[tmp[0]-1] = 1
  else:
    if a[tmp[0]-1] == tmp[1]:
      pass
    else:
      flg = 1
if n != 1 and a[0] == 0 and seen[0] == 1:
  flg = 1
if flg == 1:
  print(-1)
else:
  if a[0] == 0 and n != 1:
    a[0] = 1
  print(''.join(map(str, a)))