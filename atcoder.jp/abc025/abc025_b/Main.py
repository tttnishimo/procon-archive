n,a,b = map(int, input().split())
res = 0
for i in range(n):
  s,d = map(str, input().split())
  if s == 'East':
    res += min(max(a,int(d)),b)
  else:
    res -= min(max(a,int(d)),b)
if res > 0:
  print('East', res)
elif res == 0:
  print(0)
else:
  print('West', -res)