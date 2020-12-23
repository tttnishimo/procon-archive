h,w=map(int,input().split())
m=100
s=0
for _ in range(h):
  a=list(map(int,input().split()))
  m=min(m,min(a))
  s+=sum(a)
print(s-m*h*w)