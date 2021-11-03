N=int(input())
A=list(map(int,input().split()))
flg=0
max_flg=[0,0]
for i in range(N):
  if A[i]==1:
    flg+=1
  else:
    flg-=1
  if max_flg[1]<flg:
    max_flg=[i,flg]
if max_flg[1]==0:
  ans=A.count(1)
else:
  ans=A[:max_flg[0]+1].count(0)+A[max_flg[0]+1:].count(1)
print(ans)