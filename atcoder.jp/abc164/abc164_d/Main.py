s=list(input())
a=[0]*2019
a[0]=1
t=0
k=1
for i in range(len(s)):
  t+=int(s[-i-1])*k
  t%=2019
  a[t]+=1
  k*=10
  k%=2019
a=[(a[i]*(a[i]-1))//2 for i in range(2019)]
print(sum(a))