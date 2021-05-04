n=int(input())%26
if n==0:
  print(0)
elif n==8 or n==10:
  print(1)
elif n==16 or n==18 or n==20:
  print(2)
elif n==2 or n==4 or n==24:
  print(3)
elif n==6 or n==12 or n==14:
  print(4)
else:
  print(5)