n=int(input())
a=[1]*1000
for i in range(2,n+1):
  for j in range(2,int(i**0.5)+2):
    while i%j==0:
      i//=j
      a[j]+=1
  a[i]+=1
a[1]=1
ans=1
for i in a:
  ans*=i
  ans%=10**9+7
print(ans)