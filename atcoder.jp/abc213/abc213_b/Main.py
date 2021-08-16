N=int(input())
A=list(map(int,input().split()))
B=list(sorted(A))
print(A.index(B[-2])+1)