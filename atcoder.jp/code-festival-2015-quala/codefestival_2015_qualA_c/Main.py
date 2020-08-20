n,t=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
s=0
b=[]
flg=0
for i in range(n):
  s+=a[i][0]
  b.append(a[i][1]-a[i][0])
b.sort()
for i in range(n):
  if s<=t:
    print(i)
    flg=1
    break
  else:
    s+=b[i]
if flg==0 and s>t:
  print(-1)
elif flg==0:
  print(n)