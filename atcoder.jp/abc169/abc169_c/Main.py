a,b=map(str,input().split())
b=b[0]+b[2]+b[3]
b=int(b)
a=int(a)*b
a//=100
print(int(a))