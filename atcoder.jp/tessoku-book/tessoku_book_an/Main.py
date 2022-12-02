N=int(input())
A=list(map(int,input().split()))
B=[0]*101
for a in A:
  B[a]+=1
ans=0
for b in B:
  ans+=b*(b-1)*(b-2)//6
print(ans)