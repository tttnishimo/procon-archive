s=input()
t=input()
al=list('abcdefghijklmnopqrstuvwxyz')
a=[-1]*26
b=[-1]*26
ans='Yes'
for i in range(len(s)):
  c=al.index(s[i])
  d=al.index(t[i])
  if a[c]>=0:
    if b[d]!=c:
      ans='No'
  if b[d]>=0:
    if a[c]!=d:
      ans='No'
  if a[c]<0:
    a[c]=d
  if b[d]<0:
    b[d]=c
print(ans)