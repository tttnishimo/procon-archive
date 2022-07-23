N=int(input())
if N%4:
  x=str(N%4)+'4'*(N//4)
else:
  x='4'*(N//4)
print(sum(int(i) for i in str(int(x)*2)))
print(x)