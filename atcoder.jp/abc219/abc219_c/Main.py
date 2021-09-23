X=input()
al='abcdefghijklmnopqrstuvwxyz'
N=int(input())
S=[[input()] for _ in range(N)]
for i in range(N):
  S[i].append(''.join(al[X.index(j)] for j in S[i][0]))
S.sort(key=lambda x:x[1])
print(*[i[0] for i in S],sep='\n')