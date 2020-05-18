n=int(input())
ans=0
for i in range(2,n):
  flg=0
  for j in range(2,int(pow(i,1/2))+1):
    if i%j == 0:
      flg=1
  if flg == 0:
    ans += 1
print(ans)