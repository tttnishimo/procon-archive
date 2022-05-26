ans=[0,0,0]
input()
A=list(map(int,input().split()))
for a in A:
  ans[a-1]+=1
print(sum(i*(i-1)//2 for i in ans))