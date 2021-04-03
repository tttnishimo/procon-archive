N,K=map(int,input().split())
for i in range(K):
  N=int(''.join(sorted(list(str(N)),reverse=True)))-int(''.join(sorted(list(str(N)))))
print(N)