N,M=map(int,input().split())
if N==1:
  print(M%998244353)
elif N==2:
  print(M*(M-1)%998244353)
else:
  print(M*(M-1)*pow(M-2,N-2,998244353)%998244353)