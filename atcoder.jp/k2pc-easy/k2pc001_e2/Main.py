n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=[0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0]
for i in range(n):
  s=input()
  for j in range(7):
    if s[j]=='X':
      b[j]+=1
    else:
      b[j]=0
    c[j]=max(c[j],b[j])
c.sort(reverse=True)
for i in range(7):
  if c[i]>a[i]:
    print('NO')
    exit()
print('YES')