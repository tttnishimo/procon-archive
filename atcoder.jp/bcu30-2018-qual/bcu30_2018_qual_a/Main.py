n=int(input())
ans=[0]*(30)
a=list(map(int,input().split()))
for i in a:
  ans[i]+=1
print(*ans)