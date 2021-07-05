P=int(input())
ans=0
for i in [3628800,362880,40320,5040,720,120,24,6,2,1]:
  ans+=P//i
  P%=i
print(ans)