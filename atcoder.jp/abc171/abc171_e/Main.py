n=int(input())
a=list(map(int,input().split()))
a_xor=a[0]
ans=[]
for i in range(1,n):
  a_xor=a_xor^a[i]
for i in range(n):
  ans.append(a_xor^a[i])
print(*ans)