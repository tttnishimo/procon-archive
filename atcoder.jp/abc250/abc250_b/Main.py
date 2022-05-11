N,A,B=map(int,input().split())
for i in range(A*N):
  if (i//A)%2==0:
    print(('.'*B+'#'*B)*(N//2)+'.'*B*(N%2))
  else:
    print(('#'*B+'.'*B)*(N//2)+'#'*B*(N%2))