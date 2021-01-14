h,w=map(int,input().split())
s=['#'+input()+'#' for _ in range(h)]
s.insert(0,'#'*(w+2))
s.append('#'*(w+2))
a=['.'*(w+2) for _ in range(h+2)]
b=['.'*(w+2) for _ in range(h+2)]
for i in range(1,h+1):
  for j in range(1,w+1):
    if s[i-1][j-1:j+2]=='###' and s[i][j-1:j+2]=='###' and s[i+1][j-1:j+2]=='###':
      a[i-1]=a[i-1][:j-1]+'###'+a[i-1][j+2:]
      a[i]=a[i][:j-1]+'###'+a[i][j+2:]
      a[i+1]=a[i+1][:j-1]+'###'+a[i+1][j+2:]
      b[i]=b[i][:j]+'#'+b[i][j+1:]
flg=0
for i in range(1,h+1):
  for j in range(1,w+1):
    if a[i][j]!=s[i][j]:
      flg=1
if flg==0:
  print('possible')
  for i in range(1,h+1):
    print(*b[i][1:w+1],sep='')
else:
  print('impossible')