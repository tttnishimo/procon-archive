n=int(input())
ans=0
for i in range(1,n+1):
  a=str(i)
  b=str(oct(i))
  if a.count('7')==0 and b.count('7')==0:
    ans+=1
print(ans)