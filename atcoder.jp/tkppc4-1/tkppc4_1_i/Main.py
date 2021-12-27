import itertools
import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
C=[]
D=[]
ans=0
for i in A:
  C.append(bisect.bisect_left(B,i))
  D.append(M-bisect.bisect(B,i))
D=list(reversed(D))
D=list(itertools.accumulate(D))
D=list(reversed(D))
for i in range(N-1):
  ans+=C[i]*D[i+1]
  ans%=1000000007
print(ans)