h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
tmp=[]
for i in range(len(a)):
  for _ in range(a[i]):
    tmp.append(i+1)
ans=[]
for i in range(h):
  if i%2==0:
    print(*tmp[i*w:i*w+w])
  else:
    print(*list(reversed(tmp[i*w:i*w+w])))