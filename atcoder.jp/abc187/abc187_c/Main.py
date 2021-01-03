n=int(input())
a={}
for i in range(n):
  s=input()
  a[s]=1
  if s[0]=='!':
    s=s[1:]
  else:
    s='!'+s
  if a.get(s,0)==1:
    if s[0]=='!':
      print(s[1:])
      exit()
    else:
      print(s)
      exit()
print('satisfiable')