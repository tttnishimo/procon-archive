N=int(input())
A=list(map(int,input().split()))
for a in A:
  if A.count(a)==1:
    print(a)
    exit()