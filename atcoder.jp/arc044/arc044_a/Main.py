n = int(input())
flg = 0
sum = 0
for i in range(2, int(pow(n, 1/2))+1):
  if n % i == 0:
    flg = 1
if flg == 1:
  if n % 2 != 0 and n % 5 != 0:
    n = str(n)
    for i in range(len(n)):
      sum += int(n[i])
    if sum % 3 != 0:
      flg = 0
if flg == 0 and n != 1:
  print('Prime')
else:
  print('Not Prime')