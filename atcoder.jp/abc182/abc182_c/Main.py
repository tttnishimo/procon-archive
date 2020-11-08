n=input()
a=[0,0,0]
for i in range(len(n)):
  a[int(n[i])%3]+=1
b=[a[i]%3 for i in range(3)]
if b[1]==b[2]:
  print(0)
elif abs(b[1]-b[2])==1:
  if len(n)==1:
    print(-1)
  else:
    print(1)
elif b[1]==2:
  if a[2]>0:
    print(1)
  else:
    if len(n)==2:
      print(-1)
    else:
      print(2)
else:
  if a[1]>0:
    print(1)
  else:
    if len(n)==2:
      print(-1)
    else:
      print(2)