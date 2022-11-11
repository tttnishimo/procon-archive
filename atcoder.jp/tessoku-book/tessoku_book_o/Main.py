N=int(input())
A=list(map(int,input().split()))
B=sorted(set(A))
d={B[i]:i+1 for i in range(len(B))}
print(*[d[a] for a in A])