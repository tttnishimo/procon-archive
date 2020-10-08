n,m=map(int,input().split())
a=[]
b={}
for _ in range(m):
  k=int(input())
  if b.get(k,0)==0:
    a.insert(0,k)
    b[k]=1
  else:
    a.remove(k)
    a.insert(0,k)
for i in range(n):
  if b.get(i+1,0)==0:
    a.append(i+1)
print(*a,sep='\n')