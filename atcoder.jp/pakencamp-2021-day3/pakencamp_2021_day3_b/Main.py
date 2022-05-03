import itertools
N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
S=sum(A)
if X+Y!=S:
  print('No')
  exit()
A=A+A
a=[0]+list(itertools.accumulate(A))
a=set(a)
for i in a:
  if i+X in a or i+Y in a:
    print('Yes')
    exit()
print('No')