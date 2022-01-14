N=int(input())
ans=0
for _ in range(N):
  A,B=map(int,input().split())
  if (B-A)%10>=5:
    ans+=1
  if (B-A)%100>=50:
    ans+=1
print(ans)