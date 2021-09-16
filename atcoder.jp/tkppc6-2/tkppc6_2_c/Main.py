N=int(input())
if N==1 or N==2 or N==3 or N==6:
  print(-1)
elif N==4:
  print(2,3,2,1)
elif N==5:
  print(3,2,3,1,1)
elif N==7:
  print(4,3,2,2,1,1,1)
else:
  a=[N-3,3,2,1]+[1 if i!=N-8 else 2 for i in range(N-4)]
  print(*a)