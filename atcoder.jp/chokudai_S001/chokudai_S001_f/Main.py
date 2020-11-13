n=int(input())
a=list(map(int,input().split()))
ans=0
max_a=0
for i in a:
  if i>max_a:
    ans+=1
    max_a=i
print(ans)