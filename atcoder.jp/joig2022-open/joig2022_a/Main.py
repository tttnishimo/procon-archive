N=int(input())
A=list(map(int,input().split()))
A.sort()
print(sum(A)-A[0]-A[-1])