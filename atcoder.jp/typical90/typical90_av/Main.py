N,K=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
B=[]
for a,b in A:
  B.append(b)
  B.append(a-b)
B.sort(reverse=True)
print(sum(B[:K]))