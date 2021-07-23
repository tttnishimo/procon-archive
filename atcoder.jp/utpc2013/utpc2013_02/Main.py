Y,M=map(int,input().split())
M+=(Y-2013)*12
n=max(int((2*M)**.5)-20,1)
while True:
  if M<=n*(n+1)//2+12*n:
    print(2012+n,M-n*(n-1)//2-12*(n-1))
    break
  else:
    n+=1