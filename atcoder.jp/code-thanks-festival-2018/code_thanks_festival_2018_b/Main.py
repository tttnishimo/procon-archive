a,b=map(int,input().split())
if (a+b) % 4 == 0 and (a-(a+b)//4) % 2 == 0 and (b-(a+b)//4) % 2 == 0 and a-(a+b)//4 >= 0 and b-(a+b)//4 >= 0:
  print('Yes')
else:
  print('No')