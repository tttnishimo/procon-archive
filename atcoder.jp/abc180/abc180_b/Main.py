n=int(input())
a=list(map(int,input().split()))
b,c,d=0,0,0
for i in range(n):
  b+=abs(a[i])
  c+=a[i]**2
  d=max(d,abs(a[i]))
print(b)
print(c**0.5)
print(d)