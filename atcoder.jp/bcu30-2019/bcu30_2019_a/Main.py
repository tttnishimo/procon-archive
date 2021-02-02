n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]
a.sort(reverse=True)
print(sum(a[:k])+2*sum(a[k:]))