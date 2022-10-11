X,Y,Z=map(int,input().split())
ans=0
if X<Y<0<Z or Z<0<Y<X:
  ans=abs(X)+abs(Z)*2
elif X<Z<Y<0 or 0<Y<X<Z or 0<Y<Z<X or Z<X<Y<0:
  ans=-1
else:
  ans=abs(X)
print(ans)