S=input()
T=input()
flg=0
for i in range(len(S)-1):
  if S[i]!=T[i]:
    T=T[:i]+T[i+1]+T[i]+T[i+2:]
    break
if S==T:
  print('Yes')
else:
  print('No')