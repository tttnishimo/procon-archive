n=int(input())
ng=[]
flg=0
for _ in range(3):
  m=int(input())
  if m<n:
    ng.append(m)
  elif m==n:
    flg=1
ng.sort()
if flg==1:
  print('NO')
elif len(ng)==0:
  print('YES')
elif ng[-1]<n and ng[-1]-ng[0]==2 and len(ng)==3:
  print('NO')
else:
  ng=[ng[i]%3 for i in range(len(ng))]
  if n==300 and (0 in ng):
    print('NO')
  elif n==299 and (2 in ng) and (0 in ng):
    if ng.index(2)>ng.index(0):
      print('NO')
    else:
      print('YES')
  elif n==298 and (1 in ng) and (2 in ng) and (0 in ng):
    if ng==[0,2,1]:
      print('NO')
    else:
      print('YES')
  else:
    print('YES')