N=int(input())
l=0
r=N+1
while r>l*1.001:
  m=(r+l)/2
  if m**3+m<=N:
    l=m
  else:
    r=m
print(r)