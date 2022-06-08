N=int(input())
A=list(map(int,input().split()))
ans=[0,abs(A[1]-A[0])]
for i in range(2,N):
  ans.append(min(abs(A[i]-A[i-1])+ans[-1],abs(A[i]-A[i-2])+ans[-2]))
print(ans[-1])