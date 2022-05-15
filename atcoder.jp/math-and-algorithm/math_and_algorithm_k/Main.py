N=int(input())
ans=[]
for i in range(2,N+1):
  flg=0
  for j in range(2,int(i**.5)+1):
    if i%j==0:
      flg=1
      break
  if flg==0:
    ans.append(i)
print(*ans)