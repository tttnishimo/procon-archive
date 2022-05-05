N=int(input())
a=0
b=10**6
ans=10**18
while a<=b:
  c=a*a*a+a*a*b+a*b*b+b*b*b
  if c>=N:
    ans=min(ans,c)
    b-=1
  else:
    a+=1
print(ans)