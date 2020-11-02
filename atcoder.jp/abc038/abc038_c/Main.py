n=int(input())
a=list(map(int,input().split()))
l,r=0,0
ans=1
while r!=n-1 or l!=n-1:
  if r==n-1:
    ans+=1
    l+=1
  elif a[r+1]>a[r]:
    r+=1
    ans+=r-l
  elif r!=l:
    ans+=1
    l+=1
  else:
    r+=1
    l+=1
    ans+=1
print(ans)