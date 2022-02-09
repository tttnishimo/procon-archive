N,K=map(int,input().split())
if K<3:
  if N==1:
    print(K)
  elif N==2:
    print(K*(K-1))
  else:
    print(0)
elif N==1:
  print(K)
elif N==2:
  print(K*(K-1))
else:
  ans=K*(K-1)*pow(K-2,N-2,10**9+7)
  print(ans%(10**9+7))