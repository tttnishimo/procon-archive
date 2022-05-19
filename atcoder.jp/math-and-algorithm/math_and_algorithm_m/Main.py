N=int(input())
A=[]
for i in range(1,int(N**.5)+1):
  if N%i==0:
    A.append(i)
    if N!=i*i:
      A.append(N//i)
A.sort()
print(*A,sep='\n')