N=int(input())
A=list(map(int,input().split()))
d_l={}
d_r={}
d_l[0]=0
d_r[N+1]=0
for i in range(1,N):
  d_l[i]=max(d_l[i-1],A[i-1])
  d_r[N-i+1]=max(d_r[N-i+2],A[-i])
for _ in range(int(input())):
  L,R=map(int,input().split())
  print(max(d_l[L-1],d_r[R+1]))