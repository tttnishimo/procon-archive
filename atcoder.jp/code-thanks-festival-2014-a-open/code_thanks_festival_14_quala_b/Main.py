N=int(input())
A=[int(input()) for _ in range(3)]
A.sort(reverse=True)
ans=0
for i in range(N):
  ans+=A[i%3]
  if ans>=N:
    print(i+1)
    exit()