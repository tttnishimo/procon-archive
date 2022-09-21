import math
N=int(input())
K,M=map(int,input().split())
if N%(M//math.gcd(M,K))==0:
  print('Yes')
else:
  print('No')