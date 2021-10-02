N=int(input())
S=input()
f=0
for i in S:
  if f==0 and i=='I':
    f=1
  if f==1 and i=='O':
    f=2
  if f==2 and i=='I':
    print('Yes')
    exit()
print('No')