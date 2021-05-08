n,k=map(int,input().split())
a=list(map(str,input().split()))
for i in range(n,100000):
  if [str(i).count(j) for j in a].count(0)==k:
    print(i)
    exit()