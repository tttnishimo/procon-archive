P=list(map(int,input().split()))
al='abcdefghijklmnopqrstuvwxyz'
s=''
for i in P:
  s+=al[i-1]
print(s)