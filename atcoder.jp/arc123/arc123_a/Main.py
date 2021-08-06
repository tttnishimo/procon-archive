A=list(map(int,input().split()))
dif=2*A[1]-A[0]-A[2]
if dif>=0:
  print(dif)
elif dif%2==0:
  print(-dif//2)
else:
  print((1-dif)//2+1)