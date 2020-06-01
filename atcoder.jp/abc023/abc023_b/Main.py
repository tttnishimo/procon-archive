n=int(input())
s=input()
flg=0
for i in range((n+1)//2):
  after = s[(n-1)//2+i]
  before = s[(n-1)//2-i]
  if i % 3 == 0:
    if after != 'b' or before != 'b':
      flg = 1
  elif i % 3 == 1:
    if after != 'c' or before != 'a':
      flg = 1
  else:
    if after != 'a' or before != 'c':
      flg = 1
if flg == 1 or n % 2 == 0:
  print(-1)
else:
  print((n-1)//2)