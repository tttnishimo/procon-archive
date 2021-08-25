import itertools
S,K=map(str,input().split())
a=[]
for i in itertools.permutations(S):
  a.append(''.join(i))
a=list(set(a))
a.sort()
print(a[int(K)-1])