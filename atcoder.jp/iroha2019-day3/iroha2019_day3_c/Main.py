N,K=map(int,input().split())
A=[10**10+N-1-i for i in range(2*N-1)]
A[N-1]+=10**10
a=K-(2*N-1)
A[-1]-=a*(a+1)//2
for i in range(1,a+1):
  A.append(i)
print(*A)
print('YES')
B=[i+1 for i in range(N)]
for i in range(N-1,0,-1):
  B.append(i)
for i in range(a):
  B.append(1)
print(*B)