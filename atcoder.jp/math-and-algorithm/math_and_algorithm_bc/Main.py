N,K=map(int,input().split())
A=list(map(int,input().split()))
B=sum(abs(i) for i in A)
if K>=B and (K-B)%2==0:
  print('Yes')
else:
  print('No')