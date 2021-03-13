a,b,w=map(int,input().split())
w*=1000
c=[[a*i,b*i] for i in range(1,1000001)]
d,e=0,0
for i in range(len(c)):
  if c[i][0]<=w<=c[i][1]:
    e=max(e,i+1)
    if d==0:
      d=i+1
if d==e==0:
  print('UNSATISFIABLE')
else:
  print(d,e)