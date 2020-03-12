a,b,c = map(int, input().split())
old_abc = [a,b,c]
res = 0
flg = 0
while a%2==0 and b%2==0 and c%2==0 and flg == 0:
  tmp_a = a/2
  tmp_b = b/2
  tmp_c = c/2
  a = tmp_b + tmp_c
  b = tmp_c + tmp_a
  c = tmp_a + tmp_b
  res += 1
  if old_abc == [a,b,c]:
    flg = 1
if flg == 1:
  print(-1)
else:
  print(res)