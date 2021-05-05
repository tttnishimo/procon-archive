N,D,H=map(int,input().split())
a=[0]
for _ in range(N):
  d,h=map(int,input().split())
  a.append(h-(H-h)/(D-d)*d)
print(max(a))