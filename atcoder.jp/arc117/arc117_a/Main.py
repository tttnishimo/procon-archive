A,B=map(int,input().split())
if A>B:
  print(*[i for i in range(1,A+1)],*[i for i in range(-1,-B,-1)],-(A*(A+1)-B*(B-1))//2) 
elif A<B:
  print(*[i for i in range(1,A)],*[i for i in range(-1,-B-1,-1)],(-A*(A-1)+B*(B+1))//2)
else:
  print(*[i for i in range(1,A+1)],*[i for i in range(-1,-B-1,-1)])