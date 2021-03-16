n=int(input())
a={}
for i in range(2,int(n**0.5)+1):
  j=2
  while i**j<=n:
    if a.get(i**j,0)==0:
      a[i**j]=1
    j+=1
print(n-len(a))