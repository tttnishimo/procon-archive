N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=[]
for i in B:
  if i not in A:
    ans.append(i)
print(len(ans))
for i in ans:
  print(i)