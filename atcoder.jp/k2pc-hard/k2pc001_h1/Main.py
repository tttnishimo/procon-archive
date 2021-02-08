def aa(x,y):
  return y-(x-(y-1)*y//2-1),x-(y-1)*y//2
i,j=map(int,input().split())
a,b=0,0
for k in range(10**5):
  if k*(k+1)//2>=i:
    a+=aa(i,k)[0]
    b+=aa(i,k)[1]
    i=10**12
  if k*(k+1)//2>=j:
    a+=aa(j,k)[0]
    b+=aa(j,k)[1]
    j=10**12
print((a+b-2)*(a+b-1)//2+b)