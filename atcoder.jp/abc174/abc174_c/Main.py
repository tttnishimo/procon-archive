n=int(input())
a=7
for i in range(n):
  if a%n==0:
    print(i+1)
    break
  else:
    a%=n
    a=a*10+7
  if i==n-1:
    print(-1)