H,W=map(int,input().split())
R,C=map(int,input().split())
ans=4
if H==1 and W==1:
  ans=0
elif H==1:
  ans=2
  if C==1 or C==W:
    ans-=1
elif W==1:
  ans=2
  if R==1 or R==H:
    ans-=1
else:
  if R==1 or R==H:
    ans-=1
  if C==1 or C==W:
    ans-=1
print(ans)