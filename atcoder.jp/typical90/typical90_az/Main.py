ans=1
for i in range(int(input())):
  ans*=sum(map(int,input().split()))
  ans%=10**9+7
print(ans)