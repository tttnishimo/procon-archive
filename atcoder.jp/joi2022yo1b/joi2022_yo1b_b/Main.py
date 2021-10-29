A=int(input())
B=int(input())
A=(A+B)%12
if A==0:
  print(12)
else:
  print(A)