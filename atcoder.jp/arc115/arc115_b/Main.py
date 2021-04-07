n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
b=arr[0]
c=min(b)
for t in arr:
  tmp=b[0]-t[0]
  for i in range(n):
    if b[i]-t[i]!=tmp:
      print('No')
      exit()
  if min(t)<c:
    c=min(t)
    b=t
a=[arr[i][b.index(c)]-c for i in range(n)]
print('Yes')
print(*a)
print(*b)
