N,L=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
a=[L,0]
b=0
for x,c in reversed(A):
  a=[x,c+max(0,a[1]-(a[0]-x))]
  b=max(b,a[1])
print(b)