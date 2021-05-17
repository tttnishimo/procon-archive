N=int(input())
A=list(map(int,input().split()))
ans=[0 for _ in range(200)]
for i in A:
  ans[i%200]+=1
print(sum(i*(i-1)//2 for i in ans))