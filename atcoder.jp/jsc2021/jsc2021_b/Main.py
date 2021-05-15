N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=[]
for i in A:
  if i not in B:
    ans.append(i)
for i in B:
  if i not in A and i not in ans:
    ans.append(i)
ans.sort()
print(*ans)