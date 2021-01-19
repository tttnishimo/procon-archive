n=int(input())
a=list(map(int,input().split()))
print(a.index(min(max(a[:2**n//2]),max(a[2**n//2:])))+1)