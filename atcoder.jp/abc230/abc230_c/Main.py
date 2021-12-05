N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
for j in range(P,Q+1):
  print(*['#' if i==B-A+j or i==B+A-j else '.' for i in range(R,S+1)],sep='')