def factorization(n):
  arr=[]
  temp=n
  for i in range(2,int(-(-n**.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp//=i
      arr.append([i,cnt])
  if temp!=1:
    arr.append([temp,1])
  if arr==[]:
    arr.append([n,1])
  return arr
N,K=map(int,input().split())
A=factorization(N)
if K>sum(j for i,j in A):
  print(-1)
else:
  ans=[]
  while K>1:
    ans.append(A[0][0])
    A[0][1]-=1
    if A[0][1]==0:
      A.pop(0)
    K-=1
  if len(A)>0:
    t=1
    for i in A:
      t*=i[0]**i[1]
    ans.append(t)
  print(*ans)