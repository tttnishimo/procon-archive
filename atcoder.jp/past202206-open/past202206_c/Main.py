import math
N,M=map(int,input().split())
if N==1:
  print('o'*M)
elif N==10:
  if M<=9:
    print('o'*M)
  else:
    print('o'*9+'x'*(M-9))
else:
  n=int(math.log(10**9,N))
  if n>=M:
    print('o'*M)
  else:
    print('o'*n+'x'*(M-n))