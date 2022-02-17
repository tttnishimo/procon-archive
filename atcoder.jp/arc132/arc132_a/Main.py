n=int(input())
R=list(map(int,input().split()))
C=list(map(int,input().split()))
q=int(input())
x=''
for i in range(q):
  r,c=map(int,input().split())
  if R[r-1]+C[c-1]>=n+1:
    x+='#'
  else:
    x+='.'
print(x)