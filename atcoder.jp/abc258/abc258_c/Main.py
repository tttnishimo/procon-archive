N,Q=map(int,input().split())
S=input()
f=0
for i in range(Q):
  t,x=map(int,input().split())
  if t==1:
    f-=x
    if f<0:
      f+=N
  else:
    print(S[(f+x)%N-1])