N=int(input())
S=input()
T=S[0]
flg=0
for i in range(1,N):
  if flg==1:
    if S[i]==T[-2] and S[i] in ['a','i','u','e','o']:
      T=T[:-2]+'...'
    else:
      T+=S[i]
    flg=0
  else:
    T+=S[i]
    if S[i]=='x':
      flg=1
print(T)