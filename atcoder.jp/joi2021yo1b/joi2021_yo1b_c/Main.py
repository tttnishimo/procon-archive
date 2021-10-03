N=int(input())
A=list(map(int,input().split()))
print(sum(A[:A.index(max(A))]))
print(sum(A[A.index(max(A))+1:]))