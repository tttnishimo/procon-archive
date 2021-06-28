N=int(input())
a=[]
if N==45:
  print(1)
else:
  for i in range(180):
    for j in a:
      if 2*N*i%180==j%180:
        print(i)
        exit()
    a.append(2*N*i)