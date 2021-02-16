t=int(input())
for _ in range(t):
  l,r=map(int,input().split())
  if l==r==0:
    print(1)
  elif 2*l<=r:
    print((r-2*l+1)*(r-2*l+2)//2)
  else:
    print(0)