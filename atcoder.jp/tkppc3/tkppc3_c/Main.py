n,p=map(int,input().split())
a=list(map(int,input().split()))
m=a[0]
r=1
for l in range(n):
  if m==p:
    print('Yay!')
    exit()
  while m<=p and r<n:
    m*=a[r]
    r+=1
    if m==p:
      print('Yay!')
      exit()
  m//=a[l]
print(':(')