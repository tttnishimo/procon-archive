N=int(input())
A=list(map(int,input().split()))
ans=[A[0],A[1]]
for i in range(2,N):
  ans.append(max(ans[-2]+A[i],ans[-1]))
print(ans[-1])