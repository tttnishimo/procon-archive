n,d=map(int,input().split())
ans=0
for i in range(n):
  a,b=map(int,input().split())
  if (a*a+b*b)**(1/2)<=d:
    ans+=1
print(ans)