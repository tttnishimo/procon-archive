n=int(input())
l=len(str(n))
a=[]
s=['']
for i in range(l):
  t=[]
  for j in s:
    t.append(j+'3')
    t.append(j+'5')
    t.append(j+'7')
  s=list(t)
  a+=t
ans=len(a)
for i in a:
  if int(i)>n or '3' not in i or '5' not in i or '7' not in i:
    ans-=1
print(ans)