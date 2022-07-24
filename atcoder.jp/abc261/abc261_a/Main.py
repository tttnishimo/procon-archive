L1,R1,L2,R2=map(int,input().split())
ans=0
for i in range(101):
  if L1<=i<=R1 and L2<=i<=R2:
    ans+=1
print(max(0,ans-1))