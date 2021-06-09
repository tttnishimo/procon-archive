N=int(input())
x=[]
for _ in range(3):
  x.append(list(map(int,input().split()))+[0])
dis=[max(abs(x[i][0]-x[j][0]),abs(x[i][1]-x[j][1])) for i in range(2) for j in range(i+1,3)]
dis.sort()
for _ in range(N-3):
  y=list(map(int,input().split()))+[0]
  tmp=[max(abs(y[0]-i[0]),abs(y[1]-i[1])) for i in x]
  tmp.sort()
  dis+=[tmp[-1],tmp[-2]]
  dis.sort()
  dis=dis[-2:]
  x.append(y)
  x.sort()
  for i in range(2,len(x)-2):
    x[i][2]+=1
  x.sort(key=lambda y:y[1])
  for i in range(2,len(x)-2):
    x[i][2]+=1
  x=[i for i in x if i[2]<2]
  for i in range(len(x)):
    x[i][2]=0
print(dis[-2])