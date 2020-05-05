n = int(input())
tmp = 0
for i in range(len(str(n))):
  tmp += int(str(n)[i])
if n % tmp == 0:
  print('Yes')
else:
  print('No')
