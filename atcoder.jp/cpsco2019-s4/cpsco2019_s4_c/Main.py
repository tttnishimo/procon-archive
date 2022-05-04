import bisect
N,D=map(int,input().split())
R=list(map(int,input().split()))
R.sort()
ans=0
for i in range(N-2):
  r=bisect.bisect_right(R,R[i]+D)
  ans+=(r-1-i)*(r-2-i)//2
print(ans)