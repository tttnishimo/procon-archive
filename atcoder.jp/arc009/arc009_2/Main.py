b=list(map(str,input().split()))
n=int(input())
a=[[input()] for _ in range(n)]
for i in range(n):
  tmp_1=a[i][0]
  tmp_2=0
  while len(tmp_1)>0:
    tmp_2+=10**(len(tmp_1)-1)*b.index(tmp_1[0])
    tmp_1=tmp_1[1:]
  a[i].insert(0,tmp_2)
a.sort()
for i in a:
  print(i[1])