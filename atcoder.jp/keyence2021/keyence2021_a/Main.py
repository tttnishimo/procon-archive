n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[a[0]*b[0]]
print(c[0])
d,e=0,0
max_a=a[0]
j=0
for i in range(1,n):
  if a[i]>=a[j]:
    j=i
  if b[i]>=b[e]:
    e=i
    d=j
  else:
    if a[j]*b[i]>=c[-1]:
      d=j
      e=i
  t=a[d]*b[e]
  c.append(t)
  print(t)