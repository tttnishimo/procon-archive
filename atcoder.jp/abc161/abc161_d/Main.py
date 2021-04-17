k=int(input())
a=[1,2,3,4,5,6,7,8,9]
t=list(a)
for _ in range(10):
  s=[]
  for i in t:
    if i%10==0:
      for j in [0,1]:
        s.append(int(str(i)+str(j)))
    elif i%10==9:
      for j in [8,9]:
        s.append(int(str(i)+str(j)))
    else:
      for j in [i%10-1,i%10,i%10+1]:
        s.append(int(str(i)+str(j)))
  a+=s
  t=list(s)
print(a[k-1])