A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
ans=(B-max(A,0))*E
if A<0:
  ans+=-A*C+D
print(ans)