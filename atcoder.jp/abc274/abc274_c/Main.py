input()
A=list(map(int,input().split()))
ans=[0,0]
for a in A:
  ans+=[ans[a]+1,ans[a]+1]
print(*ans[1:],sep='\n')