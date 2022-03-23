N=int(input())
A=[i+2 for i in range(2*N)]
print(1)
for i in range(N):
  A.remove(int(input()))
  print(A.pop())