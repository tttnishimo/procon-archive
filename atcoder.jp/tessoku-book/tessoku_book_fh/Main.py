N=int(input())
ans=12
ans*=pow(7,N-1,1000000007)
ans%=1000000007
print(ans)