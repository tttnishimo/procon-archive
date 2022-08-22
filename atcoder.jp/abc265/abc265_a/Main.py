X,Y,N=map(int,input().split())
if Y>3*X:
  print(N*X)
else:
  print(N//3*Y+N%3*X)