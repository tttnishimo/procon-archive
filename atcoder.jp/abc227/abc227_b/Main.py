N=int(input())
A=list(map(int,input().split()))
B=[]
ans=0
for i in range(1,250):
  for j in range(1,250):
    B.append(4*i*j+3*(i+j))
for i in A:
  if i not in B:
    ans+=1
print(ans)