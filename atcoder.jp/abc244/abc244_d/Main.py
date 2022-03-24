S=list(input().split())
T=list(input().split())
a=0
for i in range(3):
  if S[i]==T[i]:
    a+=1
if a%3==0:
  print('Yes')
else:
  print('No')