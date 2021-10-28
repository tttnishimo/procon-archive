N=int(input())
A=list(map(int,input().split()))
X=int(input())
ans=X//sum(A)*N
X-=X//sum(A)*sum(A)
i=0
while X>=0:
  ans+=1
  X-=A[i]
  i+=1
print(ans)