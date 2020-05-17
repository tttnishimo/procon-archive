a=[0]*30
for i in range(28):
  a[int(input())-1]=1
for i,v in enumerate(a):
  if v==0:
    print(i+1)