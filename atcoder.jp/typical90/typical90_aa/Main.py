N=int(input())
d={}
for i in range(N):
  s=input()
  if d.get(s,0)==0:
    d[s]=1
    print(i+1)