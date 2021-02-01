n=int(input())*2
ans=2
for i in range(2,int(n**0.5)+1):
  if n%i==0:
    p=(n//i-1+i)//2
    q=(n//i-1-i)//2
    if (p-q)*(p+q+1)==n:
      ans+=2
print(ans)