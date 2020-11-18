n=int(input())
a=list(map(int,input().split()))
b=[0]*n
c=[]
for i in range(n):
  tmp=0
  for j in range(1,n//(n-i)+1):
    tmp+=b[(n-i)*j-1]
  if tmp%2!=a[n-i-1]:
    b[n-i-1]=1
    c.append(n-i)
c.reverse()
print(sum(b))
print(*c)