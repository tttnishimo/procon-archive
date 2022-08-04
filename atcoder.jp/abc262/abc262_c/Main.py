N=int(input())
A=list(map(int,input().split()))
ans=0
ans2=0
d={}
for i in range(N):
  if i+1==A[i]:
    ans+=1
  elif d.get(A[i],0):
    if d[A[i]]==i+1:
      ans2+=1
  else:
    d[i+1]=A[i]
print(ans*(ans-1)//2+ans2)