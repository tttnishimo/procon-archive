import math
A,B,K=map(int,input().split())
ans=''
for i in range(A+B):
  if A==0:
    C=0
  else:
    C=math.factorial(A+B-1)//(math.factorial(A-1)*math.factorial(B))
  if K<=C:
    ans+='a'
    A-=1
  else:
    ans+='b'
    B-=1
    K-=C
print(ans)