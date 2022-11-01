A=list(map(int,input().split()))
mod=998244353
A=[a%mod for a in A]
print((A[0]*A[1]*A[2]-A[3]*A[4]*A[5])%mod)