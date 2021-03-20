a=[25,39,51,76,163,111,136,128,133,138]
b=[25,39,51,76,163,111,58,128,133,138]
c=[]
for i in range(2**10):
  t1=0
  t2=0
  for j in range(10):
    t1+=a[j]*((i>>j)&1)
    t2+=b[j]*((i>>j)&1)
  if t1 not in c:
    c.append(t1)
  if t2 not in c:
    c.append(t2)
c.sort()
print(*c,sep='\n')