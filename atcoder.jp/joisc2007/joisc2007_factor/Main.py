N=int(input())
i=2
ans=dict()
n=N
while i*i<=N:
  while n%i==0:
    n=n//i
    if i in ans:
      ans[i]+=1
    else:
      ans[i]=1
  i+=1
if n!=1:
  ans[n]=1
M=list(ans.items())[-1][0]
if M>500:
  print(M)
else:
  for i in range(2,N+1):
    n=i
    for j in range(2,i+1):
      if n%j==N%j==0:
        n//=j
        N//=j
      if N==1:
        print(i)
        exit()