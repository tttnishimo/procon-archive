h,w,k=map(int,input().split())
s=[input() for _ in range(h)]
ans=[[] for _ in range(h)]
c=0
flg=[]
for i in range(h):
  if s[i].count('#')==0:
    flg.append(i)
  else:
    c+=1
    for j in range(w):
      if s[i][j]=='.':
        ans[i].append(c)
      else:
        ans[i].append(c)
        if s[i][j+1:].count('#'):
          c+=1
    for j in flg:
      ans[j]=ans[i]
    flg=[]
if flg:
  i=flg[0]-1
  for j in flg:
    ans[j]=ans[i]
for i in range(h):
  print(*ans[i])