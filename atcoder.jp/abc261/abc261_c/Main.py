N=int(input())
d={}
for i in range(N):
  S=input()
  if d.get(S,0)==0:
    print(S)
    d[S]=1
  else:
    print(S+'('+str(d[S])+')')
    d[S]+=1