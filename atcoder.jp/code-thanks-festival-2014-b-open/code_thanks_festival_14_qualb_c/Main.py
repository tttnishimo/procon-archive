n=int(input())
v=list(map(int,input().split()))
f=list(map(int,input().split()))
print(sum([1 for i in range(n) if v[i]//2<f[i]]))