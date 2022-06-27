N,X=map(int,input().split())
S=''
for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
  S+=s*N
print(S[X-1])