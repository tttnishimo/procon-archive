N=int(input())
ans=(pow(4,N+1,1000000007)-1)*pow(3,-1,1000000007)
print(ans%1000000007)