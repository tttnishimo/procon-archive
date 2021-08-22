import itertools
N,P,Q=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for a,b,c,d,e in itertools.combinations(A,5):
  ans+=int(a%P*b%P*c%P*d%P*e%P==Q)
print(ans)