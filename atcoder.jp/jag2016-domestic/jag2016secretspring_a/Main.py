t=0
for _ in range(int(input())):
  s=input()
  if s=='A':
    t+=1
  else:
    t-=1
  if t<0:
    print('NO')
    exit()
if t>0:
  print('NO')
  exit()
print('YES')