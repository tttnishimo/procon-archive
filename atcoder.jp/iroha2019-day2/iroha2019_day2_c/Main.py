N=int(input())
A=[int(input()) for _ in range(N)]
B=sorted(list(set(A)))
d={B[i]:i+1 for i in range(len(B))}
for a in A:
  print(d[a])