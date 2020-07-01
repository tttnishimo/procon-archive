A,B=map(int,input().split())
if A%4!=0:
  A+=4-A%4
B-=B%4
ans=(B-A)//4+1
for i in range(100,2000000000,100):
  if A<=i<=B and i%400!=0:
    ans-=1
print(ans)