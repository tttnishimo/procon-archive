import collections
N=int(input())
A=list(map(int,input().split()))
B=collections.Counter(A)
for i in B:
  if B[i]==3:
    print(i)
    exit()