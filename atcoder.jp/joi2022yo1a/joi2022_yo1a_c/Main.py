N=int(input())
S=input()
ans=0
for a in ['A','B','C','D','E']:
  if S.count(a):
    ans+=1
if ans>2:
  print('Yes')
else:
  print('No')