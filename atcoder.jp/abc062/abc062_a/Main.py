a,b = map(int, input().split())
g_1 =[1,3,5,7,8,10,12]
g_2 = [4,6,9,11]
if (a in g_1 and b in g_1) or (a in g_2 and b in g_2) or (a == 2 and b == 2):
  print('Yes')
else:
  print('No')