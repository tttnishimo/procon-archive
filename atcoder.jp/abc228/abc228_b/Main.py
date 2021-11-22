N,X=map(int,input().split())
A=list(map(int,input().split()))
B=set()
x=X
while x not in B:
  B.add(x)
  x=A[x-1]
print(len(B))