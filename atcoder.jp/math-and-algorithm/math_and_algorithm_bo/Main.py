N,X,Y=map(int,input().split())
for a in range(1,N+1):
  for b in range(1,N+1):
    for c in range(1,N+1):
      if Y%a==0 and Y%a%b==0 and Y%a%b%c==0:
        if Y//a//b//c<=N and a+b+c+Y//a//b//c==X:
          print('Yes')
          exit()
print('No')