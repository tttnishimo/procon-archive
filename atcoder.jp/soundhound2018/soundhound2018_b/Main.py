n,L,R=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for i in A:
  if i<L:
    B.append(L)
  elif i>R:
    B.append(R)
  else:
    B.append(i)
print(*B)