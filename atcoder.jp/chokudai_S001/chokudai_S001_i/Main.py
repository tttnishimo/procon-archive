n=int(input())
a=list(map(int,input().split()))
m=len(a)
l,r=0,1
ans=0
while l!=m:
  t=sum(a[l:r])
  if r!=m:
    if n==t:
      ans+=1
      r+=1
    elif n>t:
      r+=1
    else:
      l+=1
      if r==l:
        r+=1
  else:
    if n==t:
      ans+=1
      l+=1
    elif n<t:
      l+=1
    else:
      break
print(ans)