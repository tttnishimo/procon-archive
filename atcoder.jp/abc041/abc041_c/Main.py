n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(n):
  ans.append([a[i],i+1])
ans.sort(reverse=True)
for i in ans:
  print(i[1])