N=int(input())
L=len(str(N))
ans=0
for i in range(1,L+1):
  for j in range(L):
    M=int('1'*i+'0'*j)
    M2=int('1'*(i-1)+'2'+'0'*j)
    if N>=M:
      ans+=min(N+1,M2)-M
print(ans)