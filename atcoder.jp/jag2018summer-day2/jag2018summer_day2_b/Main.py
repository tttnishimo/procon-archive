import itertools
N=int(input())
a=[1,5,10,50,100,500]
b=[True]*10001
if N>14:
  print(500)
else:
  for i in range(14):
    cnt=0
    for j in itertools.combinations_with_replacement(a,i+1):
      if b[sum(j)]:
        b[sum(j)]=False
        cnt+=1
    if i==N-1:
      print(cnt)