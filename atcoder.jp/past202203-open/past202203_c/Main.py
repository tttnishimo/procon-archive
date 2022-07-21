A=input()
a=-1
al='abcdefghijklmnopqrstuvwxyz'
while len(A)>3:
  a+=1
  A=A[:-3]
print(A+al[a])