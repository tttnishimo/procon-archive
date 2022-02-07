N=int(input())
A=list(map(int,input().split()))
l=[0]
for i in A:
  l.append((l[-1]+i)%360)
l.sort()
l.append(360)
ans=0
for i in range(N+1):
  ans=max(ans,l[i+1]-l[i])
print(ans)