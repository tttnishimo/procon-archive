na,nb=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s={}
for i in b:
  s[i]=1
t=[]
for i in a:
  if s.get(i,0)==0:
    s[i]=1
  else:
    t.append(i)
print(len(t)/len(s))