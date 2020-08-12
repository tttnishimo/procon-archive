n,m=map(int,input().split())
al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=input()
t=input()
s1=[0]*26
t1=[0]*26
ans=0
for i in range(26):
  s1[i]=s.count(al[i])
  t1[i]=t.count(al[i])
for i in range(26):
  if s1[i]>=1 and t1[i]==0:
    ans=-1
  elif ans>=0 and s1[i]>=1:
    ans=max(ans,-(-s1[i]//t1[i]))
print(ans)