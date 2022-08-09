import itertools
N,M=map(int,input().split())
for i in itertools.combinations(range(1,M+1),N):
  print(*i)