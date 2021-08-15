H,W,N=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
h=list(sorted(set([i[0] for i in A])))
w=list(sorted(set([i[1] for i in A])))
d_h,d_w={},{}
for i,j in enumerate(h):
  d_h[j]=i+1
for i,j in enumerate(w):
  d_w[j]=i+1
for i in A:
  print(d_h[i[0]],d_w[i[1]])