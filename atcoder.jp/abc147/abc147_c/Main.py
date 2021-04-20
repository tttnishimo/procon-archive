n=int(input())
a=[]
ans=0
for _ in range(n):
  m=int(input())
  a.append([list(map(int,input().split())) for _ in range(m)])
for i in range(2**n):
  flg=0
  for j in range(n):
    if i>>j&1:
      for k in a[j]:
        if ((i>>(k[0]-1))-k[1])&1:
          flg=1
  if flg==0:
    ans=max(ans,str(bin(i)).count('1'))
print(ans)