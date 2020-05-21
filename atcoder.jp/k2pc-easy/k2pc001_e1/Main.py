a=list(map(int,input().split()))
n=int(input())
print(max(n-a[0],0), max(n*2-a[1],0), max(n*3-a[2],0))