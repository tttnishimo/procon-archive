N=int(input())
A=list(map(int,input().split()))
print(sum(max(0,i-10) for i in A))