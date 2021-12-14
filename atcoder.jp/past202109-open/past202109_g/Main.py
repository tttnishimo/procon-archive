import sys
readline = sys.stdin.readline
N,K=map(int,input().split())
A=[tuple(map(int,input().split())) for _ in range(N)]
ng,ok=0,10**18+1

def is_ok(X,K):
  t=0
  for a,b,c in A:
    if X>=b:
      t+=min((X-b)//c+1,a)
  if t>=K:
    return True
  return False

while abs(ok-ng)>1:
  m=abs(ok+ng)//2
  if is_ok(m,K):
    ok=m
  else:
    ng=m
print(ok)