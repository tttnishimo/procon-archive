n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(n):
  tmp=i
  for j in range(n):
    if a[tmp] == i+1:
      ans.append(j+1)
      break
    else:
      tmp=a[tmp]-1
print(*ans)