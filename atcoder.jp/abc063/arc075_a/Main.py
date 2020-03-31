n = int(input())
sum = 0
tmp_2 = 101
for i in range(n):
  tmp = int(input())
  sum += tmp
  if tmp % 10 != 0:
    tmp_2 = min(tmp_2,tmp)
if sum % 10 != 0:
  print(sum)
elif tmp_2 == 101:
  print(0)
else:
  print(sum - tmp_2)