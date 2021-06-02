import itertools
N=int(input())
S=input()
for i in itertools.permutations(S):
  flg=0
  for j in range(N):
    if i[j]!=S[j]:
      flg+=1
      break
  for j in range(N):
    if i[j]!=S[-j-1]:
      flg+=1
      break
  if flg==2:
    print(*i,sep='')
    exit()
print('None')