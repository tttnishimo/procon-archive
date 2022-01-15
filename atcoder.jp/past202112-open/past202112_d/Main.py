N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[[-A[i]-B[i],-A[i],i] for i in range(N)]
C=sorted(C,key=lambda x:(x[0],x[1],x[2]))
print(*[k+1 for i,j,k in C])