import collections
N=int(input())
A=list(map(int,input().split()))
a=collections.Counter(A)
ans=[20000,101]
for i in a.items():
  if ans[1]>i[1]:
    ans=i
  elif ans[1]==i[1] and ans[0]>i[0]:
    ans=i
print(ans[0])