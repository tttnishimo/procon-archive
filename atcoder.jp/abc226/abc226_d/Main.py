import math
N=int(input())
A=[list(map(int, input().split())) for _ in range(N)]
ans=set()
for i in range(N-1):
  for j in range(i+1,N):
    s=A[i][0]-A[j][0]
    t=A[i][1]-A[j][1]
    g=math.gcd(abs(s),abs(t))
    ans.add((s//g,t//g))
    ans.add((-s//g,-t//g))
print(len(ans))