N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
a=[0]*46
b=[0]*46
c=[0]*46
for i in A:
  a[i%46]+=1
for i in B:
  b[i%46]+=1
for i in C:
  c[i%46]+=1
ans=0
for i,j in enumerate(a):
  for k,l in enumerate(b):
    for m,n in enumerate(c):
      if (i+k+m)%46==0:
        ans+=j*l*n
print(ans)