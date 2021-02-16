n=int(input())
a=0
ans=0
for _ in range(n):
  a+=int(input())
  if a<=2018:
    ans+=1
print(ans)