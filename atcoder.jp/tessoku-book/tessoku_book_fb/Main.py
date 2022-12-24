N=int(input())
ans=[]
for i in range(1,int(N**.5)+1):
  if N%i==0:
    ans.append(i)
    if i*i!=N:
      ans.append(N//i)
ans.sort()
print(*ans,sep='\n')