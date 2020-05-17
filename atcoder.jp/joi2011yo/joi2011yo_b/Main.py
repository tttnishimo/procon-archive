s=input()
n=int(input())
ans=0
for i in range(n):
  tmp=input()*2
  if s in tmp:
    ans+=1
print(ans)