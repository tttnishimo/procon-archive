n=int(input())
s=[input() for _ in range(n)]
a,b,ab=0,0,0
ans=0
for i in s:
  if i[0]=='B':
    b+=1
  if i[-1]=='A':
    a+=1
  if i[0]=='B' and i[-1]=='A':
    ab+=1
  ans+=i.count('AB')
if ab==a and ab==b and ab!=0:
  ans-=1
print(ans+min(a,b))