N=int(input())
A=[list(input()) for _ in range(N)]
ans=''
for i in range(N//2):
  flg=0
  for j in A[i]:
    if flg==0 and j in A[-i-1]:
      ans=ans+j
      flg=1
  if flg==0:
    print(-1)
    exit()
if N%2:
  ans=ans+A[N//2][0]+''.join(reversed(ans))
else:
  ans=ans+''.join(reversed(ans))
print(ans)