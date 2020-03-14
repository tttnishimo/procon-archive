n = int(input())
tmp = 0
if n % 9 == 0:
  m = 9
else:
  m = n % 9
for i in range(6):
  if n > i * 9:
    tmp += 10 ** i
print(m * tmp)