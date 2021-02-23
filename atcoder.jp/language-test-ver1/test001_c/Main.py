s=list(map(str,input().split()))
a=[]
n=int(input())
for _ in range(n):
  t=input()
  u=''
  for i in range(len(t)):
    u+=str(s.index(t[i]))
  a.append([int(u),t])
a.sort()
for i in range(n):
  print(a[i][1])