N,M=map(int,input().split())
S=list(map(str,input().split()))
T=set(map(str,input().split()))
for i in S:
  if i in T:
    print('Yes')
  else:
    print('No')