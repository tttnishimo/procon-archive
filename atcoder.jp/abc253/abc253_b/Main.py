H,W=map(int,input().split())
S=[input() for _ in range(H)]
h=-1
w=0
for i in range(H):
  if S[i].count('o')==2:
    print(W-''.join(reversed(S[i])).index('o')-S[i].index('o')-1)
    exit()
  elif S[i].count('o')==1 and h==-1:
    h=i
    w=S[i].index('o')
  elif S[i].count('o')==1:
    print(i-h+abs(S[i].index('o')-w))
    exit()