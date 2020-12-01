n=int(input())
a=max(0,int((2*(n+1))**0.5)-10)
for i in range(a,a+20):
  if i*(i+1)//2==n+1:
    print(n-i+1)
    break
  elif i*(i+1)//2>n+1:
    print(n-i+2)
    break