X,A,D,N=map(int,input().split())
min_a=min(A,A+D*(N-1))
max_a=max(A,A+D*(N-1))
if X<=min_a:
  print(min_a-X)
elif X>=max_a:
  print(X-max_a)
else:
  d=abs(X-A)//abs(D)
  d1=A+D*d
  d2=d1+D
  print(min(abs(X-d1),abs(X-d2)))