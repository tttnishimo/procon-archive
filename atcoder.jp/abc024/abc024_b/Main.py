n,t = map(int, input().split())
tmp_1 = 0
tmp_2 = 0
res = 0
for i in range(n):
  tmp_2 = int(input())
  if tmp_1 == 0:
    pass
  elif tmp_1 + t < tmp_2:
    res += t
  else:
    res += tmp_2 - tmp_1
  tmp_1 = tmp_2
res += t
print(res)