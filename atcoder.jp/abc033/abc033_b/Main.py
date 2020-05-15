n = int(input())
a = []
b = []
flg = -1
for i in range(n):
  s,m = map(str,input().split())
  a.append(s)
  b.append(int(m))
for i in range(n):
  if b[i] > sum(b)/2:
    flg = i
if flg == -1:
  print('atcoder')
else:
  print(a[flg])