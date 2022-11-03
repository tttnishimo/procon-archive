import itertools
H,W=map(int,input().split())
X=[[0]+list(itertools.accumulate(list(map(int,input().split())))) for _ in range(H)]
for _ in range(int(input())):
  A,B,C,D=map(int,input().split())
  print(sum(X[i][D]-X[i][B-1] for i in range(A-1,C)))