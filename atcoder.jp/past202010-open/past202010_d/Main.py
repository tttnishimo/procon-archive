N=int(input())
S=input()
a=[[0,0] for _ in range(N)]
for i in range(N):
  if S[i]=='.':
    if S[:i].count('#') and S[i:].count('#'):
      a[i]=[list(reversed(S[:i+1])).index('#'),S[i:].index('#')]
    elif not S[:i].count('#') and S[i:].count('#'):
      a[i]=[50,S[i:].index('#')]
    elif S[:i].count('#') and not S[i:].count('#'):
      a[i]=[list(reversed(S[:i+1])).index('#'),50]
for i in range(50):
  for j in range(i+1):
    t=(i-j,j)
    flg=0
    for k in a:
      if t[0]<k[0] and t[1]<k[1]:
        flg=1
    if flg==0:
      print(t[1],t[0])
      exit()