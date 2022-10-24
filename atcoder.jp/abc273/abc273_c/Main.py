import collections
N=int(input())
A=list(map(int,input().split()))
B=list(A)+[0]
B.sort(reverse=True)
S=collections.Counter(A)
M=0
for i in range(N):
  if B[i]!=B[i+1]:
    print(S[B[i]])
  else:
    M+=1
for i in range(M):
  print(0)