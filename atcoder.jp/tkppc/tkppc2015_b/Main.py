n=int(input())
a=[int(input()) for _ in range(n)]
print(a.index(max(a))+1)