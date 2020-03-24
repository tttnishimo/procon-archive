n,m = map(int, input().split())
a = [[0, 'WA'] for i in range(n)]
tmp_AC = 0
tmp_WA = 0
for i in range(m):
  l,s = map(str, input().split())
  l = int(l) - 1
  if a[l][1] == 'WA' and s == 'AC':
    a[l][1] = 'AC'
    tmp_AC += 1
    tmp_WA += a[l][0]
  elif a[l][1] == 'WA' and s == 'WA':
    a[l][0] += 1
print(tmp_AC, tmp_WA)