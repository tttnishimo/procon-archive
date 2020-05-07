a,b = map(int, input().split())
res = 0
for i in range(a,b+1):
  i = str(i)
  flg = 0
  for j in range(len(i)//2):
    if i[j] != i[-j-1]:
      flg = 1
  if flg == 0:
    res += 1
print(res)