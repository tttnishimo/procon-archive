K=int(input())
A,B=map(str,input().split())
a,b=0,0
for i in range(len(A)):
  a+=int(A[-i-1])*K**i
for i in range(len(B)):
  b+=int(B[-i-1])*K**i
print(a*b)