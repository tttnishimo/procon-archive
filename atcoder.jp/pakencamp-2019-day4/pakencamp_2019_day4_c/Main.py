L1,R1=map(int,input().split())
L2,R2=map(int,input().split())
L3,R3=map(int,input().split())
ans=0
for i in range(L1,R1+1):
  ans+=min(max((R2-i)/(R2-L2+1),0),1)*min(max((R3-i)/(R3-L3+1),0),1)/(R1-L1+1)
print(ans)