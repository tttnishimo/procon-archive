n,q=map(int,input().split())
a=[list(map(str,input().split())) for _ in range(n)]
a=[[int(a[i][0]),a[i][1]] for i in range(n)]
a.insert(0,[0,'kogakubu10gokan'])
a.append([100,''])
i=0
while True:
  if a[i+1][0]>q:
    print(a[i][1])
    break
  i+=1