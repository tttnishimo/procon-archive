N,P=map(int,input().split())
A=list(map(int,input().split()))
ans=[1 if i<P else 0 for i in A]
print(sum(ans))