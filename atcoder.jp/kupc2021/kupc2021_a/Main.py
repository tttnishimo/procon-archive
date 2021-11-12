N=int(input())
S=list(map(int,input().split()))
T=int(input())
print(len(set(i//T for i in S)))