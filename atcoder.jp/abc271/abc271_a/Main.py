N=hex(int(input()))
if len(N)==3:
  print('0'+N[-1].upper())
else:
  print(N[-2:].upper())