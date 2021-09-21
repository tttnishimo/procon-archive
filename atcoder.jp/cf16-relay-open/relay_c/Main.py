N=int(input())
a=[int(input()) for _ in range(2**N)]
while len(a)!=1:
  b=[abs(a[2*i]-a[2*i+1]) if a[2*i]!=a[2*i+1] else a[2*i] for i in range(len(a)//2)]
  a=list(b)
print(a[0])