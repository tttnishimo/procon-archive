N=int(input())
a=[]
ans=0
for _ in range(N):
  t,l,r=map(int,input().split())
  if t==1:
    a.append([l,r])
  elif t==2:
    a.append([l,r-.1])
  elif t==3:
    a.append([l+.1,r])
  else:
    a.append([l+.1,r-.1])
for i in range(N-1):
  for j in range(i+1,N):
    if (a[i][0]<=a[j][0] and a[i][1]>=a[j][0]) or (a[j][0]<=a[i][0] and a[j][1]>=a[i][0]) or (a[i][0]>=a[j][0] and a[i][1]<=a[j][1]):
      ans+=1
print(ans)