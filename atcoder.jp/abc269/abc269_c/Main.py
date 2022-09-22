N=int(input())
ans=[0]
for i in range(len(bin(N))-2):
  t=[]
  if N>>i&1:
    for j in ans:
      t.append(2**i+j)
    ans+=t
print(*ans,sep='\n')