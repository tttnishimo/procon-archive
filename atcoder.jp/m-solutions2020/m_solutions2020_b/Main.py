a,b,c=map(int,input().split())
k=int(input())
c*=2**k
for i in range(k-1):
  if a<b<c:
    break
  c//=2
  b*=2
if a<b<c:
  print('Yes')
else:
  print('No')