n=int(input())
a=list(map(int,input().split()))
print(sum([a[i]*2**(n-1-i) for i in range(n)]))