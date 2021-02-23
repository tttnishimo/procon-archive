p=int(input())
if p==1:
  print(1)
else:
  f=[1,1]
  for i in range(15000000):
    f.append(f[-1]+f[-2])
    if f[-1]%p==0:
      print(i+3)
      exit()
  print(-1)