S=input()
T=input()
a=[[S[0],0]]
b=[[T[0],0]]
for s in S:
  if s==a[-1][0]:
    a[-1][1]+=1
  else:
    a.append([s,1])
for t in T:
  if t==b[-1][0]:
    b[-1][1]+=1
  else:
    b.append([t,1])
if len(a)!=len(b):
  print('No')
else:
  for i in range(len(a)):
    if a[i][0]!=b[i][0]:
      print('No')
      exit()
    elif a[i][1]>b[i][1]:
      print('No')
      exit()
    elif a[i][1]!=b[i][1] and a[i][1]==1:
      print('No')
      exit()
  print('Yes')