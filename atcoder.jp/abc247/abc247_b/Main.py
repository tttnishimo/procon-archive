N=int(input())
A=[list(input().split()) for _ in range(N)]
l=[]
for i in A:
  l.append(i[0])
  l.append(i[1])
if len(set(l))<N*2-1:
  print('No')
else:
  print('Yes')