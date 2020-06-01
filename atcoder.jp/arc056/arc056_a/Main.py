a,b,k,l=map(int,input().split())
print(min(k//l*b+b,k//l*b+a*(k-k//l*l)))