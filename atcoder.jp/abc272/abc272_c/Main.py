N=int(input())
A=list(map(int,input().split()))
A1=[a for a in A if a%2]
A2=[a for a in A if a%2==0]
A1.sort()
A2.sort()
ans=-1
if len(A1)>1:
  ans=max(ans,A1[-1]+A1[-2])
if len(A2)>1:
  ans=max(ans,A2[-1]+A2[-2])
print(ans)