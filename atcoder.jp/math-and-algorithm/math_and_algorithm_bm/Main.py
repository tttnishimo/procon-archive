N=int(input())
ans=N//10000
N%=10000
ans+=N//5000
N%=5000
ans+=N//1000
print(ans)