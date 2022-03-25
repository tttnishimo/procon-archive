S=input()
al='abcdefghijklmnopqrstuvwxyz'
a=[0]*26
for i in S:
  a[al.index(i)]+=1
t=0
for i in a:
  if t==0 and i!=0:
    t=i
  if i!=t and i!=0:
    print('No')
    exit()
print('Yes')