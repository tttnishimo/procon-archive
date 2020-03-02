n = int(input())
li = list(map(int,input().split()))
error = 0
for i in range(n):
  if li[i]%2 == 0:
    if li[i]%3 == 0 or li[i]%5 == 0:
      pass
    else:
      error = 1
  else:
    pass
if error:
  print('DENIED')
else:
  print('APPROVED')