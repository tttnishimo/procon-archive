n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
flg=0
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if a[j][0]-a[i][0]==0 and a[k][0]-a[i][0]==0:
        flg=1
      elif a[j][0]-a[i][0]==0 or a[k][0]-a[i][0]==0:
        pass
      elif (a[j][1]-a[i][1])/(a[j][0]-a[i][0])==(a[k][1]-a[i][1])/(a[k][0]-a[i][0]):
        flg=1
if flg==1:
  print('Yes')
else:
  print('No')