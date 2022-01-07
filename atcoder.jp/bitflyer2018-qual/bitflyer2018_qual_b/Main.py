A,B,N=map(int,input().split())
S=input()
for i in S:
  if i=='S' and A:
    A-=1
  elif i=='C' and B:
    B-=1
  elif i=='E' and A and A>=B:
    A-=1
  elif i=='E' and B>A:
    B-=1
print(A)
print(B)