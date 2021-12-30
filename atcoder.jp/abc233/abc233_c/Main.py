N,X=map(int,input().split())
A=list(map(int,input().split()))[1:]
for _ in range(N-1):
  B=list(map(int,input().split()))[1:]
  t=[]
  for a in A:
    for b in B:
      t.append(a*b)
  A=t
print(A.count(X))