N=int(input())
for i in range(1,60):
  if 2**i-1==N:
    print('Second')
    exit()
else:
  print('First')