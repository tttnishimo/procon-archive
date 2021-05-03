n=int(input())
ans=0
for i in range(1,int(n**0.5)+1000):
  if int(str(i)*2)<=n:
    ans+=1
print(ans)