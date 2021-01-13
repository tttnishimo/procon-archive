from collections import Counter
n,c=map(int,input().split())
a=[]
b=[]
for i in range(n):
  if i%2==0:
    a.append(int(input()))
  else:
    b.append(int(input()))
a=Counter(a).most_common()
b=Counter(b).most_common()
if a[0][0]==b[0][0]:
  if len(a)==1 or len(b)==1:
    print(c*b[0][1])
  else:
    print(c*(n-max(a[1][1]+b[0][1],a[0][1]+b[1][1])))
else:
  print(c*(n-a[0][1]-b[0][1]))