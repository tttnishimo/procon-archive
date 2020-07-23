n=int(input())
a=list(map(int,input().split()))
s=sum(a)
ans=n-1
if s%n!=0:
  print(-1)
else:
  flg=1
  for i in range(n-1):
    if sum(a[:i+1])/(i+1)==s//n:
      ans-=1
      for j in range(i+1):
        a[j]=s//n
    else:
      flg+=1
  print(ans)