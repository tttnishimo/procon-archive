N=int(input())
ans=0
for i in range(N+1):
  ans+=i
  if ans>=N:
    print(i)
    exit()