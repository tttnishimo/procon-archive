N=int(input())
A=list(map(int,input().split()))
MOD=10**9+7
fib=[1,1]
for i in range(N-2):
  fib.append((fib[-1]+fib[-2])%MOD)
ans=A[0]*(fib[-1]+fib[-2])
ans%=MOD
for i in range(1,N):
  ans+=A[i]*(fib[-i]*fib[i]-fib[-i-1]*fib[i-1])
  ans%=MOD
if N==1:
  print(A[0])
else:
  print(ans)