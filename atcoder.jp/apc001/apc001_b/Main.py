n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[b[i]-a[i] for i in range(n)]
if sum([(c[i]+1)//2 for i in range(n) if c[i]>0])<=sum(b)-sum(a):
  print('Yes')
else:
  print('No')