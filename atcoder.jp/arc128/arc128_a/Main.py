N=int(input())
A=list(map(int,input().split()))
tmp=A[0]
ans=[]
up=1
for i in range(1,N):
  if up==1:
    if A[i]>=tmp:
      ans.append(0)
    else:
      up=-1
      ans.append(1)
  else:
    if A[i]<=tmp:
      ans.append(0)
    else:
      up=1
      ans.append(1)
  tmp=A[i]
if up==-1:
  ans.append(1)
else:
  ans.append(0)
print(*ans)