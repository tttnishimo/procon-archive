import numpy as np
def powmtx(mtx,n,M):
  if n==1:
    return mtx
  m2,p2=mtx,2
  while p2<n:
    m2=(m2*m2)%M
    p2*=2
  return powmtx(mtx,n-p2//2,M)*m2%M
N=int(input())
a=np.matrix([[2,1],[1,0]])
ans=(powmtx(a,N-2,10**9+7)*np.matrix([[1],[1]]))[0]
print(int(ans)%(10**9+7))