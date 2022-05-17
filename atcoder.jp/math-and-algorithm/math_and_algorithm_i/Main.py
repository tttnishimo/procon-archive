N,S=map(int,input().split())
A=list(map(int,input().split()))
B={0}
for a in A:
  C=[]
  for b in B:
    if a+b<=S:
      C.append(a+b)
  for c in C:
    B.add(c)
if S in B:
  print('Yes')
else:
  print('No')