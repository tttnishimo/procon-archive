n=input()
l=len(n)
ans=0
for i in range(l):
  t=10**(l-1-i)*2**i
  for j in range(l-1-i):
    t+=10**j*2**(l-2-j)
  ans+=int(n[i])*t
print(ans)