n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
b=sorted(a)
c=sorted(a,key=lambda x: x[1])
if b[0]==c[0]:
  print(min(max(b[0][0],c[1][1]),max(b[1][0],c[0][1]),b[0][0]+b[0][1]))
else:
  print(min(max(b[0][0],c[0][1]),b[0][0]+b[0][1],c[0][0]+c[0][1]))