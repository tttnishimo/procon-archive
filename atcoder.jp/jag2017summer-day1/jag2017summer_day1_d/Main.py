X,Y,Z=map(int,input().split())
a=1-Z/((X*X+Y*Y)**.5)
print(X-X*a/(2-a))