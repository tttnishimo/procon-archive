k=int(input())
ans=0
for i in range(1,int(k**0.5)+1):
  for j in range(i,k//i+1):
    ans+=max(0,(k//(i*j)-j+1))*6
    if i==j and i**3<=k:
      ans-=5
    else:
      if i**2*j<=k:
        ans-=3
      if i*j**2<=k:
        ans-=3
print(ans)